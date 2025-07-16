let chatbotSteps = [];
let chatbotState = 0;

// Рендер одного шага сценария
function renderChatbotStep(stepIdx) {
  const step = chatbotSteps[stepIdx];
  const messages = document.getElementById('chatbot-messages');
  const buttons = document.getElementById('chatbot-buttons');
  if (!step) return;

  // Если это прощальный шаг (нет кнопок), показываем только прощальное сообщение на чистом экране
  if (!step.buttons || step.buttons.length === 0) {
    messages.innerHTML = `<div style="margin-bottom:8px;">${step.text}</div>`;
    buttons.innerHTML = '';
    setTimeout(() => {
      document.getElementById('chatbot-window').style.display = 'none';
      messages.innerHTML = '';
      chatbotState = 0;
    }, 2000);
    return;
  }

  // Добавить сообщение
  messages.innerHTML += `<div style="margin-bottom:8px;">${step.text}</div>`;
  messages.scrollTop = messages.scrollHeight;

  // Кнопки
  buttons.innerHTML = '';
  step.buttons.forEach(btn => {
    if (btn.url) {
      // Ссылка-кнопка (телефон, WhatsApp, Telegram)
      const a = document.createElement('a');
      a.textContent = btn.label;
      a.href = btn.url;
      if (btn.url.startsWith('http')) {
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
      }
      // Убираем inline-стили, используем только CSS
      a.className = "chatbot-link-btn";
      buttons.appendChild(a);
    } else {
      // Обычная кнопка (переход по сценарию)
      const b = document.createElement('button');
      b.textContent = btn.label;
      b.onclick = () => {
        if (btn.next === null) {
          // Закрыть чат
          document.getElementById('chatbot-window').style.display = 'none';
          messages.innerHTML = '';
          chatbotState = 0;
        } else if (
          chatbotSteps[btn.next] &&
          (!chatbotSteps[btn.next].buttons || chatbotSteps[btn.next].buttons.length === 0)
        ) {
          // Если это кнопка "Нет, спасибо" (ведёт на прощальный шаг), показываем только прощание на чистом экране
          messages.innerHTML = `<div style="margin-bottom:8px;">${chatbotSteps[btn.next].text}</div>`;
          document.getElementById('chatbot-buttons').innerHTML = '';
          setTimeout(() => {
            document.getElementById('chatbot-window').style.display = 'none';
            messages.innerHTML = '';
            chatbotState = 0;
          }, 2000);
        } else {
          renderChatbotStep(btn.next);
          chatbotState = btn.next;
        }
      };
      buttons.appendChild(b);
    }
  });

  // Форма для ввода телефона
  if (step.input) {
    const input = document.createElement('input');
    input.type = 'tel';
    input.placeholder = '+7 (___) ___-__-__';
    buttons.appendChild(input);
    const sendBtn = document.createElement('button');
    sendBtn.textContent = 'Отправить';
    sendBtn.style = "margin: 8px 0 0 0; display:block;";
    sendBtn.onclick = () => {
      if (input.value.trim().length < 10) {
        alert('Пожалуйста, введите корректный номер.');
        return;
      }
      messages.innerHTML += `<div style="margin-bottom:8px;">Спасибо! Мы свяжемся с вами в ближайшее время.</div>`;
      buttons.innerHTML = '';
      setTimeout(() => {
        document.getElementById('chatbot-window').style.display = 'none';
        messages.innerHTML = '';
        chatbotState = 0;
      }, 2500);
    };
    buttons.appendChild(sendBtn);
  }
}

// Загрузка сценария и инициализация кнопки открытия
window.addEventListener('DOMContentLoaded', function() {
  // Проверяем, что кнопка существует
  const toggle = document.getElementById('chatbot-toggle');
  if (!toggle) return;
  fetch('/chatbot_scenario')
    .then(response => response.json())
    .then(data => {
      chatbotSteps = data;
      toggle.onclick = function() {
        const win = document.getElementById('chatbot-window');
        if (win.style.display === 'none' || win.style.display === '') {
          win.style.display = 'block';
          document.getElementById('chatbot-messages').innerHTML = '';
          document.getElementById('chatbot-buttons').innerHTML = '';
          renderChatbotStep(0);
          chatbotState = 0;
        } else {
          win.style.display = 'none';
          document.getElementById('chatbot-messages').innerHTML = '';
          document.getElementById('chatbot-buttons').innerHTML = '';
          chatbotState = 0;
        }
      };
    });
});
