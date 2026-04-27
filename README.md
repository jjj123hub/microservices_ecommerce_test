# 微服务在线商城质量保障项目

## 项目概述
这是一个基于微服务架构的电商系统质量保障项目，包含 UI 自动化测试、API 契约测试、性能测试和 Redis 热点 Key 优化等。

## 技术栈
- **UI自动化**: Playwright + pytest
- **契约测试**: Pact
- **性能测试**: k6, Locust
- **缓存优化**: Redis
- **测试报告**: Allure
- **数据库**: MySQL

## 项目结构
```
microservices_ecommerce_test/
├── config/              # 配置文件
│   └── settings.py      # 配置和定位器
├── pages/               # Page Object Model
│   ├── base_page.py     # 基类
│   ├── login_page.py    # 登录页
│   ├── product_page.py  # 商品页
│   └── checkout_page.py # 结账页
├── utils/               # 工具类
│   ├── redis_helper.py  # Redis助手
│   └── db_helper.py     # 数据库助手
├── tests/               # 测试用例
│   ├── test_login.py    # 登录测试
│   ├── test_purchase.py # 购买流程测试
│   ├── test_redis.py    # Redis测试
│   └── test_pact.py     # 契约测试
├── performance/         # 性能测试
│   ├── locustfile.py    # Locust脚本
│   └── k6_script.js     # k6脚本
├── conftest.py          # pytest配置
├── requirements.txt     # 依赖包
└── README.md
```

## 核心原理详解

### 1. Playwright 自动化框架
**原理**: Playwright 是微软开发的新一代自动化测试工具，支持多浏览器（Chromium、Firefox、WebKit）。

**核心优势**:
- **自动等待**: 元素可交互时才执行操作，减少 flaky tests
- **多浏览器支持**: 同一套代码运行在不同浏览器
- **网络拦截**: 可以 mock API 响应，便于测试各种场景
- **追踪功能**: 完整记录测试执行过程，便于调试

**关键特性**:
- 自动等待元素可见、可点击
- 支持 Shadow DOM
- 支持多标签页、多上下文
- 内置截图、录屏功能

### 2. 契约测试 (Contract Testing)
**原理**: 确保服务消费者和提供者之间的 API 契约保持一致，防止集成问题。

**Pact 工作流程**:
1. **消费者端**: 编写测试，定义期望的请求和响应
2. **生成契约**: 运行消费者测试，生成 Pact 文件（JSON格式）
3. **提供者验证**: 将契约文件交给提供者，验证是否满足契约

**优势**:
- 提前发现 API 变更问题
- 减少集成测试成本
- 支持独立部署

### 3. 性能测试与优化
**原理**: 通过模拟高并发请求，评估系统性能瓶颈并进行优化。

**k6 特点**:
- 基于 Go 语言，性能优异
- 使用 JavaScript 编写测试脚本
- 支持多种协议（HTTP、WebSocket、gRPC）
- 丰富的指标和阈值设置

**Redis 热点 Key 优化**:
- **热点 Key 检测**: 分析 TTL、访问频率
- **优化策略**:
  - 本地缓存（L1 Cache）
  - Key 分片
  - 读写分离
  - 限流熔断

### 4. 微服务架构下的测试策略
**分层测试金字塔**:
- **UI 测试**: 覆盖核心业务流程（10%）
- **服务集成测试**: 验证服务间交互（30%）
- **单元测试**: 验证单个函数逻辑（60%）

**测试关注点**:
- 服务可用性
- 数据一致性
- 故障隔离
- 性能指标（P99响应时间、QPS）

## 运行测试

```bash
# 安装依赖
pip install -r requirements.txt
playwright install

# 运行 UI 测试
pytest tests/ -v --alluredir=allure-results

# 生成 Allure 报告
allure serve allure-results

# 运行 k6 性能测试
k6 run performance/k6_script.js

# 运行 Locust
locust -f performance/locustfile.py
```

## 性能优化效果
- 接口响应时间 P99: 1.2s → 320ms
- 回归测试效率提升: 80%
- 联调问题减少: 70%
- 缺陷解决率: 100%
