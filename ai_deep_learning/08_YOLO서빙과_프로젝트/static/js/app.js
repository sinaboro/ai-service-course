// FloatWatch 화면 동작: 폼을 서버로 보내고, 받은 결과로 화면 바꾸기
const form = document.querySelector('#detect-form');
const statusText = document.querySelector('#status');
const resultImg = document.querySelector('#result-img');
const caption = document.querySelector('#result-caption');
const rows = document.querySelector('#result-rows');

function setStatus(message, isError = false) {
  statusText.textContent = message;
  statusText.classList.toggle('error', isError);
}

function showResult(data) {
  resultImg.src = data.image;                              // 서버가 그린 결과 이미지
  resultImg.alt = '탐지 결과: 객체 ' + data.count + '개';
  caption.textContent = '객체 ' + data.count + '개 탐지 · 처리 시간 ' + data.seconds + '초';
  rows.replaceChildren();                                  // 표 비우기
  for (const b of data.boxes) {
    const tr = document.createElement('tr');
    for (const text of [b.class, b.conf.toFixed(2)]) {
      const td = document.createElement('td');
      td.textContent = text;                               // textContent: 글자로만 넣기 (안전)
      tr.append(td);
    }
    rows.append(tr);
  }
}

async function send(formData) {
  setStatus('탐지 중...');
  try {
    const res = await fetch('/detect', { method: 'POST', body: formData });
    const data = await res.json();
    if (!res.ok) {
      setStatus('오류: ' + data.detail, true);
      return;
    }
    showResult(data);
    setStatus('완료!');
  } catch (err) {
    setStatus('서버에 연결할 수 없어요. 서버가 켜져 있나요?', true);
  }
}

form.addEventListener('submit', (event) => {
  event.preventDefault();                                  // 페이지 이동 막기
  send(new FormData(form));                                // file, conf 를 그대로 담기
});

document.querySelector('#sample-btn').addEventListener('click', async () => {
  const blob = await (await fetch('/static/images/sample.png')).blob();
  const formData = new FormData();
  formData.append('file', blob, 'sample.png');
  formData.append('conf', document.querySelector('#conf').value);
  send(formData);
});

// 주소 끝에 ?sample 을 붙여 열면 샘플을 자동으로 탐지 (교안 캡처용)
if (new URLSearchParams(location.search).has('sample')) {
  document.querySelector('#sample-btn').click();
}
