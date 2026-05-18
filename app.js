const STORAGE_KEY = 'water-academy-tests';
const LEGACY_STORAGE_KEY = 'rut-miit-tests';

const sampleTests = [
  {
    id: crypto.randomUUID(),
    title: 'Основы безопасности на водном транспорте',
    topic: 'Безопасность',
    description: 'Демонстрационный тест для проверки работы системы тестирования.',
    questions: [
      {
        text: 'Что нужно сделать перед началом практического занятия на воде?',
        answers: ['Проверить технику безопасности', 'Сразу приступить к заданию', 'Отключить средства связи'],
        correct: 0,
      },
      {
        text: 'Можно ли проходить тесты без регистрации?',
        answers: ['Да', 'Нет'],
        correct: 0,
      },
      {
        text: 'Где создаются новые тесты?',
        answers: ['В отдельной админ-панели', 'На странице результатов', 'В поисковой строке'],
        correct: 0,
      },
    ],
  },
];

let tests = loadTests();
let currentTest = null;
let currentQuestion = 0;
let userAnswers = [];

const catalogScreen = document.querySelector('#catalog-screen');
const runnerScreen = document.querySelector('#runner-screen');
const testList = document.querySelector('#test-list');
const searchInput = document.querySelector('#search-input');
const runner = document.querySelector('#runner');

document.querySelector('#back-to-catalog').addEventListener('click', showCatalog);
searchInput.addEventListener('input', renderCatalog);

renderCatalog();

function loadTests() {
  const stored = localStorage.getItem(STORAGE_KEY) || localStorage.getItem(LEGACY_STORAGE_KEY);
  if (!stored) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(sampleTests));
    return sampleTests;
  }

  try {
    const parsed = JSON.parse(stored);
    if (Array.isArray(parsed)) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(parsed));
      return parsed;
    }
  } catch {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(sampleTests));
  }

  return sampleTests;
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
  tests = loadTests();
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

  runner.innerHTML = `
    <article class="result-card">
      <p class="eyebrow">Результат</p>
      <h2>${escapeHtml(currentTest.title)}</h2>
      <div class="result-score">${percent}%</div>
      <p>Правильных ответов: <strong>${correctCount}</strong> из <strong>${currentTest.questions.length}</strong></p>
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
}

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}
