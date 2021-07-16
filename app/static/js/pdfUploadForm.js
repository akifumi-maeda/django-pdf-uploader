// 要素の取得
const form = document.querySelector('form');
const fileInputField = document.querySelector('input[type="file"]');
const fileInputButton = document.querySelector('.file-input-button');

// input-group用のdiv要素の作成
const div = document.createElement('div');
div.setAttribute('class', 'input-group my-4');

// フィールドとボタンをdivでラップ
form.appendChild(div);
div.appendChild(fileInputField);
div.appendChild(fileInputButton);