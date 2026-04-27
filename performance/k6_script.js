import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend } from 'k6/metrics';

let responseTimeTrend = new Trend('response_time');

export let options = {
    stages: [
        { duration: '30s', target: 50 },
        { duration: '1m', target: 100 },
        { duration: '30s', target: 0 },
    ],
    thresholds: {
        'http_req_duration': ['p(95)<500', 'p(99)<1200'],
    },
};

export default function () {
    let res = http.get('http://localhost:8003/products');
    
    check(res, {
        'status is 200': (r) => r.status === 200,
        'response time < 500ms': (r) => r.timings.duration < 500,
    });
    
    responseTimeTrend.add(res.timings.duration);
    sleep(1);
}
