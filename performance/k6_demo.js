import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  vus: 100,
  duration: '30s',
  thresholds: {
    'http_req_duration': ['p(95)<500', 'p(99)<1000'],
  },
};

export default function () {
  // 访问 Saucedemo 首页（不会失败！）
  let res = http.get('https://www.saucedemo.com');

  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  sleep(1);
}