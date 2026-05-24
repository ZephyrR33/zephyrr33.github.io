const STORAGE_KEY = 'water-academy-tests';
const LEGACY_STORAGE_KEY = 'rut-miit-tests';
const ADMIN_LOGIN = 'rut123';
const ADMIN_PASSWORD = 'miit2026';
const CONFIG = window.APP_CONFIG || {};
const API_BASE_URL = (CONFIG.API_BASE_URL || '').replace(/\/$/, '');

let tests = [];

const adminLock = document.querySelector('#admin-lock');
const adminPanel = document.querySelector('#admin-panel');
const questionsBox = document.querySelector('#questions');
const questionTemplate = document.querySelector('#question-template');
const form = document.querySelector('#test-form');

document.querySelector('#login-button').addEventListener('click', login);
document.querySelector('#logout-button').addEventListener('click', logout);
document.querySelector('#add-question').addEventListener('click', () => addQuestionEditor());
document.querySelector('#reset-form').addEventListener('click', resetForm);
document.querySelector('#export-tests').addEventListener('click', exportTestsJson);
form.addEventListener('submit', saveFromForm);

init();

async function init() {
  tests = await loadTests();
  renderAdminList();
  addQuestionEditor();
  restoreAdminSession();
}

async function loadTests() {
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

async function persist() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tests));
  if (!API_BASE_URL) return true;

  const response = await fetch(`${API_BASE_URL}/api/tests`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Admin-Login': ADMIN_LOGIN,
      'X-Admin-Password': ADMIN_PASSWORD,
    },
    body: JSON.stringify(tests),
  });

  return response.ok;
}

function login() {
  const loginValue = document.querySelector('#admin-login').value.trim();
  const password = document.querySelector('#admin-password').value;

  if (loginValue !== ADMIN_LOGIN || password !== ADMIN_PASSWORD) {
    alert('Неверный логин или пароль.');
    return;
  }

  sessionStorage.setItem('water-academy-admin', 'true');
  adminLock.hidden = true;
  adminPanel.hidden = false;
}

function restoreAdminSession() {
  if (sessionStorage.getItem('water-academy-admin') !== 'true') return;
  adminLock.hidden = true;
  adminPanel.hidden = false;
}

function logout() {
  sessionStorage.removeItem('water-academy-admin');
  adminPanel.hidden = true;
  adminLock.hidden = false;
  document.querySelector('#admin-login').value = '';
  document.querySelector('#admin-password').value = '';
}

function addQuestionEditor(question = { text: '', answers: ['', ''], correct: 0 }) {
  const fragment = questionTemplate.content.cloneNode(true);
  const editor = fragment.querySelector('.question-editor');
  editor.querySelector('.question-text').value = question.text;
  editor.querySelector('.remove-question').addEventListener('click', () => {
    editor.remove();
    renumberQuestions();
  });
  editor.querySelector('.add-answer').addEventListener('click', () => addAnswerRow(editor));

  questionsBox.appendChild(fragment);
  question.answers.forEach((answer, index) => addAnswerRow(questionsBox.lastElementChild, answer, question.correct === index));
  renumberQuestions();
}

function addAnswerRow(editor, value = '', checked = false) {
  const answers = editor.querySelector('.answers');
  const row = document.createElement('div');
  row.className = 'answer-row';
  row.innerHTML = `
    <input type="radio" name="correct-${editor.dataset.index || Date.now()}" ${checked ? 'checked' : ''} title="Правильный ответ">
    <input class="answer-text" type="text" required placeholder="Вариант ответа" value="${escapeAttribute(value)}">
    <button class="icon-button remove-answer" type="button" title="Удалить вариант">×</button>
  `;
  row.querySelector('.remove-answer').addEventListener('click', () => row.remove());
  answers.appendChild(row);
  renumberQuestions();
}

function renumberQuestions() {
  questionsBox.querySelectorAll('.question-editor').forEach((editor, index) => {
    editor.dataset.index = index;
    editor.querySelector('h4').textContent = `Вопрос ${index + 1}`;
    editor.querySelectorAll('input[type="radio"]').forEach((radio) => {
      radio.name = `correct-${index}`;
    });
  });
}

async function saveFromForm(event) {
  event.preventDefault();
  const builtQuestions = [...questionsBox.querySelectorAll('.question-editor')].map((editor) => {
    const rows = [...editor.querySelectorAll('.answer-row')];
    const answers = rows.map((row) => row.querySelector('.answer-text').value.trim());
    const correct = rows.findIndex((row) => row.querySelector('input[type="radio"]').checked);
    return {
      text: editor.querySelector('.question-text').value.trim(),
      answers,
      correct,
    };
  });

  if (builtQuestions.some((question) => !question.text || question.answers.length < 2 || question.answers.some((answer) => !answer) || question.correct < 0)) {
    alert('Заполните текст каждого вопроса, минимум два варианта ответа и отметьте правильный вариант.');
    return;
  }

  const test = {
    id: document.querySelector('#test-id').value || crypto.randomUUID(),
    title: document.querySelector('#test-title').value.trim(),
    topic: document.querySelector('#test-topic').value.trim(),
    description: document.querySelector('#test-description').value.trim(),
    questions: builtQuestions,
  };

  const existingIndex = tests.findIndex((item) => item.id === test.id);
  if (existingIndex >= 0) {
    tests[existingIndex] = test;
  } else {
    tests.unshift(test);
  }

  const saved = await persist();
  renderAdminList();
  resetForm();

  if (saved && API_BASE_URL) {
    alert('Тест сохранен на сервере ПК. Его увидят все, пока сервер и туннель работают.');
    return;
  }

  if (saved) {
    alert('Тест сохранен локально. Чтобы его увидели все студенты на GitHub Pages, скачайте tests.json и замените этот файл в репозитории.');
    return;
  }

  alert('Тест сохранен в браузере, но сервер ПК не ответил. Проверьте туннель и backend.');
}

function renderAdminList() {
  const adminTests = document.querySelector('#admin-tests');
  if (!tests.length) {
    adminTests.innerHTML = '<p class="empty">Список тестов пуст.</p>';
    return;
  }

  adminTests.innerHTML = tests
    .map(
      (test) => `
        <div class="admin-item">
          <div>
            <strong>${escapeHtml(test.title)}</strong>
            <p class="muted">${escapeHtml(test.topic)} · ${test.questions.length} вопрос(ов)</p>
          </div>
          <div class="admin-actions">
            <button class="secondary-button" type="button" data-edit="${test.id}">Редактировать</button>
            <button class="danger-button" type="button" data-delete="${test.id}">Удалить</button>
          </div>
        </div>
      `,
    )
    .join('');

  adminTests.querySelectorAll('[data-edit]').forEach((button) => {
    button.addEventListener('click', () => editTest(button.dataset.edit));
  });
  adminTests.querySelectorAll('[data-delete]').forEach((button) => {
    button.addEventListener('click', () => deleteTest(button.dataset.delete));
  });
}

function editTest(id) {
  const test = tests.find((item) => item.id === id);
  if (!test) return;

  document.querySelector('#test-id').value = test.id;
  document.querySelector('#test-title').value = test.title;
  document.querySelector('#test-topic').value = test.topic;
  document.querySelector('#test-description').value = test.description;
  questionsBox.innerHTML = '';
  test.questions.forEach((question) => addQuestionEditor(question));
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

async function deleteTest(id) {
  if (!confirm('Удалить этот тест?')) return;
  tests = tests.filter((test) => test.id !== id);
  await persist();
  renderAdminList();
}

function exportTestsJson() {
  const json = JSON.stringify(tests, null, 2);
  const blob = new Blob([json], { type: 'application/json;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'tests.json';
  link.click();
  URL.revokeObjectURL(url);
}

function resetForm() {
  form.reset();
  document.querySelector('#test-id').value = '';
  questionsBox.innerHTML = '';
  addQuestionEditor();
}

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

function escapeAttribute(value) {
  return escapeHtml(value).replaceAll('`', '&#096;');
}
