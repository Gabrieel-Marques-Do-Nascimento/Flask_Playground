// import { user } from './export.mjs';
import { user } from 'http://127.0.0.1:5000/export';

const msg = document.getElementById("mensagem");
msg.innerHTML = user()
// curl http://127.0.0.1:5000/export
