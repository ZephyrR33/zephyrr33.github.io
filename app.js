const STORAGE_KEY = 'water-academy-tests';
const LEGACY_STORAGE_KEY = 'rut-miit-tests';
const API_URL_STORAGE_KEY = 'water-academy-api-url';
const CONFIG = window.APP_CONFIG || {};
const API_BASE_URL = resolveApiBaseUrl();
const FIREBASE_DB_URL = (CONFIG.FIREBASE_DB_URL || '').replace(/\/$/, '');
const RESULT_EMAIL = CONFIG.RESULT_EMAIL || 'teacher@example.com';

let tests = [];
let currentTest = null;
let currentQuestion = 0;
let userAnswers = [];

function resolveApiBaseUrl() {
  const params = new URLSearchParams(window.location.search);
  const apiFromUrl = params.get('api');
  if (apiFromUrl) {
    const normalized = apiFromUrl.replace(/\/$/, '');
    localStorage.setItem(API_URL_STORAGE_KEY, normalized);
    return normalized;
  }

  return (localStorage.getItem(API_URL_STORAGE_KEY) || CONFIG.API_BASE_URL || '').replace(/\/$/, '');
}

const catalogScreen = document.querySelector('#catalog-screen');
const runnerScreen = document.querySelector('#runner-screen');
const testList = document.querySelector('#test-list');
const searchInput = document.querySelector('#search-input');
const runner = document.querySelector('#runner');

document.querySelector('#back-to-catalog').addEventListener('click', showCatalog);
searchInput.addEventListener('input', renderCatalog);

init();

async function init() {
  tests = await loadTests();
  renderCatalog();
}

async function loadTests() {
  const firebaseTests = await loadFirebaseTests();
  if (firebaseTests.length) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(firebaseTests));
    return firebaseTests;
  }

  const apiTests = await loadApiTests();
  if (apiTests.length) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(apiTests));
    return apiTests;
  }

  const sharedTests = await loadSharedTests();
  if (sharedTests.length) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(sharedTests));
    return sharedTests;
  }

  const stored = localStorage.getItem(STORAGE_KEY) || localStorage.getItem(LEGACY_STORAGE_KEY);
  if (!stored) return [];

  try {
    const parsed = JSON.parse(stored);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

async function loadFirebaseTests() {
  if (!FIREBASE_DB_URL) return [];

  try {
    const response = await fetch(`${FIREBASE_DB_URL}/tests.json`, { cache: 'no-store' });
    if (!response.ok) return [];
    const parsed = await response.json();
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

async function loadApiTests() {
  if (!API_BASE_URL) return [];

  try {
    const response = await fetch(`${API_BASE_URL}/api/tests`, { cache: 'no-store' });
    if (!response.ok) return [];
    const parsed = await response.json();
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

async function loadSharedTests() {
  try {
    const response = await fetch('tests.json', { cache: 'no-store' });
    if (!response.ok) return [];
    const parsed = await response.json();
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

function showCatalog() {
  runnerScreen.classList.remove('is-visible');
  catalogScreen.classList.add('is-visible');
}

function showRunner() {
  catalogScreen.classList.remove('is-visible');
  runnerScreen.classList.add('is-visible');
}

function renderCatalog() {
  const query = searchInput.value.trim().toLowerCase();
  const filtered = tests.filter((test) => `${test.title} ${test.topic} ${test.description}`.toLowerCase().includes(query));

  if (!filtered.length) {
    testList.innerHTML = '<p class="empty">Тестов пока нет. Преподаватель может создать их в админ-панели.</p>';
    return;
  }

  testList.innerHTML = filtered
    .map(
      (test) => `
        <article class="test-card">
          <div class="meta">
            <span class="pill">${escapeHtml(test.topic)}</span>
            <span>${test.questions.length} вопрос(ов)</span>
          </div>
          <h3>${escapeHtml(test.title)}</h3>
          <p class="muted">${escapeHtml(test.description || 'Описание не добавлено.')}</p>
          <button class="primary-button" type="button" data-start="${test.id}">Пройти тест</button>
        </article>
      `,
    )
    .join('');

  testList.querySelectorAll('[data-start]').forEach((button) => {
    button.addEventListener('click', () => startTest(button.dataset.start));
  });
}

function startTest(id) {
  currentTest = tests.find((test) => test.id === id);
  if (!currentTest) return;
  currentQuestion = 0;
  userAnswers = Array(currentTest.questions.length).fill(null);
  showRunner();
  renderQuestion();
}

function renderQuestion() {
  const question = currentTest.questions[currentQuestion];
  const progress = Math.round(((currentQuestion + 1) / currentTest.questions.length) * 100);

  runner.innerHTML = `
    <article class="runner-card">
      <div class="runner-top">
        <div>
          <p class="eyebrow">${escapeHtml(currentTest.topic)}</p>
          <h2>${escapeHtml(currentTest.title)}</h2>
        </div>
        <span class="pill">${currentQuestion + 1} из ${currentTest.questions.length}</span>
      </div>
      <div class="progress" aria-label="Прогресс"><span style="width: ${progress}%"></span></div>
      <h3>${escapeHtml(question.text)}</h3>
      <div>
        ${question.answers
          .map(
            (answer, index) => `
              <label class="option">
                <input type="radio" name="answer" value="${index}" ${userAnswers[currentQuestion] === index ? 'checked' : ''}>
                <span>${escapeHtml(answer)}</span>
              </label>
            `,
          )
          .join('')}
      </div>
      <div class="runner-actions">
        <button class="primary-button" type="button" id="next-question">${currentQuestion === currentTest.questions.length - 1 ? 'Завершить' : 'Следующий вопрос'}</button>
      </div>
    </article>
  `;

  runner.querySelector('#next-question').addEventListener('click', nextQuestion);
}

function nextQuestion() {
  const selected = runner.querySelector('input[name="answer"]:checked');
  if (!selected) {
    alert('Выберите вариант ответа.');
    return;
  }

  userAnswers[currentQuestion] = Number(selected.value);

  if (currentQuestion < currentTest.questions.length - 1) {
    currentQuestion += 1;
    renderQuestion();
    return;
  }

  renderResult();
}

function renderResult() {
  const correctCount = currentTest.questions.reduce((sum, question, index) => {
    return sum + (question.correct === userAnswers[index] ? 1 : 0);
  }, 0);
  const percent = Math.round((correctCount / currentTest.questions.length) * 100);
  const resultText = buildResultText(correctCount, percent);

  runner.innerHTML = `
    <article class="result-card">
      <p class="eyebrow">Результат</p>
      <h2>${escapeHtml(currentTest.title)}</h2>
      <div class="result-score">${percent}%</div>
      <p>Правильных ответов: <strong>${correctCount}</strong> из <strong>${currentTest.questions.length}</strong></p>
      <label>
        ФИО студента
        <input id="student-name" type="text" placeholder="Введите фамилию и имя" />
      </label>
      <button class="secondary-button" type="button" id="send-result">Отправить результат</button>
      <div class="review">
        ${currentTest.questions
          .map((question, index) => {
            const isCorrect = question.correct === userAnswers[index];
            return `
              <div class="review-item ${isCorrect ? '' : 'is-wrong'}">
                <p><strong>${isCorrect ? 'Верно' : 'Ошибка'}</strong></p>
                <p>${escapeHtml(question.text)}</p>
                <p class="muted">Ваш ответ: ${escapeHtml(question.answers[userAnswers[index]])}</p>
                <p class="muted">Правильный ответ: ${escapeHtml(question.answers[question.correct])}</p>
              </div>
            `;
          })
          .join('')}
      </div>
      <button class="primary-button" type="button" id="finish-review">Вернуться к тестам</button>
    </article>
  `;

  runner.querySelector('#finish-review').addEventListener('click', showCatalog);
  runner.querySelector('#send-result').addEventListener('click', () => submitResult(correctCount, percent, resultText));
}

function buildResultText(correctCount, percent) {
  const lines = [
    'Результат тестирования',
    `Тест: ${currentTest.title}`,
    `Тема: ${currentTest.topic}`,
    `Результат: ${percent}%`,
    `Правильных ответов: ${correctCount} из ${currentTest.questions.length}`,
    '',
    'Ответы:',
  ];

  currentTest.questions.forEach((question, index) => {
    const userAnswer = question.answers[userAnswers[index]];
    const correctAnswer = question.answers[question.correct];
    lines.push(`${index + 1}. ${question.text}`);
    lines.push(`Ответ студента: ${userAnswer}`);
    lines.push(`Правильный ответ: ${correctAnswer}`);
    lines.push('');
  });

  return lines.join('\n');
}

async function submitResult(correctCount, percent, resultText) {
  const studentName = document.querySelector('#student-name').value.trim() || 'Студент';
  const payload = {
    studentName,
    testId: currentTest.id,
    testTitle: currentTest.title,
    topic: currentTest.topic,
    correctCount,
    total: currentTest.questions.length,
    percent,
    resultText,
    answers: currentTest.questions.map((question, index) => ({
      question: question.text,
      studentAnswer: question.answers[userAnswers[index]],
      correctAnswer: question.answers[question.correct],
      isCorrect: question.correct === userAnswers[index],
    })),
  };

  if (API_BASE_URL) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/results`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (response.ok) {
        alert('Результат отправлен и сохранен.');
        return;
      }
    } catch {
      // Fallback to email client below.
    }
  }

  if (FIREBASE_DB_URL) {
    try {
      const response = await fetch(`${FIREBASE_DB_URL}/results.json`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...payload, createdAt: new Date().toISOString() }),
      });

      if (response.ok) {
        alert('Результат сохранен.');
        return;
      }
    } catch {
      // Fallback to email client below.
    }
  }

  sendResultEmail(studentName, resultText);
}

function sendResultEmail(studentName, resultText) {
  const subject = `Результат теста: ${studentName}`;
  const body = `ФИО студента: ${studentName}\n\n${resultText}`;
  window.location.href = `mailto:${encodeURIComponent(RESULT_EMAIL)}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}
