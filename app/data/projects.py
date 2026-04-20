PROJECT_THEMES = [
    {
        "id": "nelow-ai",
        "title": "NELOW 누수음센서 탐지 AI",
        "subtitle": "IoT Acoustic Leak Detection AI System",
        "color": "#3b82f6",
        "icon": "water_drop",
        "period": "2025.02 ~ 현재",
        "team": "BE 2 / FE 1 / AI 1",
        "contribution": "AI 기여도 100%",

        # ── 1. Project Overview ──
        "summary": "수도계량기·관로·밸브에 부착된 IoT 음수집 센서로 24시간 수집한 음향 데이터를 CNN 모델로 분석하여 누수 여부를 자동 판별하는 AI 시스템",
        "role": "AI 모델 E2E 개발 (데이터 전처리 → 특징 추출 → 모델 설계/학습 → 평가 → 배포)",
        "tech_stack": {
            "AI/ML": ["TensorFlow", "Keras", "LibROSA", "scikit-learn"],
            "Infra": ["MLflow", "MinIO(S3)", "MySQL", "Docker"],
            "Analysis": ["NumPy", "Pandas", "Matplotlib", "Folium"],
            "Deploy": ["SSH/SFTP", "TFLite", "Edge AI"],
        },
        "metrics": [
            {"value": "2,801+", "label": "학습 샘플"},
            {"value": "3", "label": "분류 클래스"},
            {"value": "91.44%", "label": "Val Accuracy"},
            {"value": "8개국", "label": "글로벌 배포"},
        ],

        # ── 2. Background & Objective ──
        "background": {
            "pain_points": [
                "숙련된 청음 전문가가 수도계량기·관로·밸브에 청음봉을 직접 대고 누수 여부를 판단하는 방식",
                "전문가의 경험과 감에 의존 → 인력 부족, 주관적 판단, 비효율적 현장 점검",
                "비가청 대역(고주파) 누수는 사람이 감지 불가",
            ],
            "goals": [
                "IoT 음수집 센서를 수도계량기·관로·밸브에 부착하여 24시간 자동 음향 데이터 수집 체계 구축",
                "수집된 음데이터를 AI로 분석하여 전문가 의존 없이 객관적·자동화된 누수 진단",
                "다양한 소음 환경(전기음, 기계음, 동물 소리)에서도 안정적 정확도 확보",
            ],
            "before": [
                {"step": "전문가 현장 방문", "icon": "person_search"},
                {"step": "수도계량기·관로·밸브에\n청음봉 대고 청취", "icon": "hearing"},
                {"step": "경험 기반\n주관적 판단", "icon": "psychology_alt"},
                {"step": "느림 / 비용 높음", "icon": "trending_down"},
            ],
            "after": [
                {"step": "수도계량기·관로·밸브에\nIoT 센서 부착", "icon": "sensors"},
                {"step": "24시간\n자동 음수집", "icon": "graphic_eq"},
                {"step": "AI 분석\n객관적 판별", "icon": "verified"},
                {"step": "실시간 / 저비용", "icon": "trending_up"},
            ],
        },

        # ── 3. Core Strategy & Implementation ──
        "pipeline_steps": [
            {"icon": "sensors", "label": "WAV 수집", "sub": "M2 IoT 센서", "color": "#06b6d4"},
            {"icon": "speed", "label": "8kHz 리샘플링", "sub": "표준화", "color": "#64748b"},
            {"icon": "content_cut", "label": "1초 추출", "sub": "최소 에너지 구간", "color": "#64748b"},
            {"icon": "tune", "label": "밴드패스 필터", "sub": "50 ~ 2000Hz", "color": "#f59e0b"},
            {"icon": "graphic_eq", "label": "MEL 스펙트로그램", "sub": "128 x 16 x 1", "color": "#8b5cf6"},
            {"icon": "psychology", "label": "CNN 모델", "sub": "Conv2D x3 → Dense", "color": "#3b82f6"},
            {"icon": "verified", "label": "누수 판별", "sub": "L / H / N", "color": "#10b981"},
        ],
        "preprocess_steps": [
            {"label": "원본 WAV", "sub": "현장 IoT 센서 수집 데이터", "color": "#64748b"},
            {"label": "8kHz 리샘플링", "sub": "표준 샘플레이트로 통일", "color": "#64748b"},
            {"label": "최소 표준편차 1초 구간 선택", "sub": "0.1초 윈도우 분할 → 가장 안정적인 1초 자동 선택", "color": "#06b6d4"},
            {"label": "Butterworth BPF (5차, 50~2000Hz)", "sub": "차량 소음·저주파 진동 제거, 누수 대역 집중", "color": "#f59e0b"},
            {"label": "전기음 탐지 (Welch PSD)", "sub": "Spectral Flatness ≤ 0.30 & Hum Ratio ≥ 0.30 → Notch 필터 제거", "color": "#ef4444", "branch": True},
            {"label": "클린 오디오 출력", "sub": "MEL 스펙트로그램 변환 준비 완료", "color": "#10b981"},
        ],

        "architecture_mermaid": "",
        "preprocessing_mermaid": """graph TD
    A["원본 WAV"] --> B["8kHz 리샘플링"]
    B --> C["0.1초 윈도우 분할"]
    C --> D["최소 표준편차<br/>1초 구간 선택"]
    D --> E["Butterworth BPF<br/>5차, 50~2000Hz"]
    E --> F{"전기음 탐지<br/>Welch PSD"}
    F -->|"감지됨"| G["Notch 필터<br/>고조파 제거"]
    F -->|"정상"| H["클린 오디오"]
    G --> H

    style A fill:#64748b,stroke:#475569,color:#fff
    style F fill:#f59e0b,stroke:#d97706,color:#fff
    style H fill:#10b981,stroke:#059669,color:#fff""",

        "technical_choices": [
            {"choice": "MEL Spectrogram", "reason": "사람의 청각 인지 특성 반영, 2D CNN 입력에 최적화된 시간-주파수 표현"},
            {"choice": "밴드패스 50~2000Hz", "reason": "차량 소음·전기 험 제거, 누수 음향 주파수 대역에 집중"},
            {"choice": "최소 에너지 1초 추출", "reason": "과도 응답·돌발 잡음 자동 제거, 안정적인 분석 구간 확보"},
            {"choice": "LeakyReLU(α=0.1)", "reason": "Dying ReLU 방지, 음수 영역 그래디언트 보존으로 학습 안정성 향상"},
            {"choice": "MLflow + MinIO", "reason": "모델 버전 관리·재현성 보장·데이터셋 계보 추적"},
        ],

        "cnn_architecture": [
            {"layer": "Input", "output": "(128, 16, 1)", "detail": "MEL 스펙트로그램"},
            {"layer": "Conv2D(32) + LeakyReLU + MaxPool", "output": "(64, 8, 32)", "detail": "저수준 특징 추출"},
            {"layer": "Conv2D(64) + LeakyReLU + MaxPool", "output": "(32, 4, 64)", "detail": "중간 특징 추출"},
            {"layer": "Conv2D(128) + LeakyReLU + MaxPool", "output": "(16, 2, 128)", "detail": "고수준 특징 추출"},
            {"layer": "Flatten", "output": "(4,096)", "detail": "1D 벡터 변환"},
            {"layer": "Dense(128) + LeakyReLU", "output": "(128)", "detail": "분류 특징 압축"},
            {"layer": "Dense(3) + Softmax", "output": "(3)", "detail": "L / H / N 분류"},
        ],

        "key_works": [
            {
                "title": "신호 전처리 파이프라인",
                "icon": "tune",
                "color": "#06b6d4",
                "desc": "전기음 자동 감지 및 제거",
                "tags": ["Welch PSD", "Notch Filter", "BPF", "Spectral Flatness"],
            },
            {
                "title": "CNN 모델 반복 고도화",
                "icon": "psychology",
                "color": "#8b5cf6",
                "desc": "V8-1 → V8-2 → V8-2-3 진화",
                "tags": ["Conv2D x3", "EarlyStopping", "Cross Validation", "Stratified Split"],
            },
            {
                "title": "MLflow 실험 관리 체계",
                "icon": "science",
                "color": "#f59e0b",
                "desc": "모델·데이터셋 버전 자동 추적",
                "tags": ["MLflow", "MinIO S3", "Artifact 관리", "Baseline 비교"],
            },
        ],

        # ── 4. Obstacles & Troubleshooting ──
        "challenges": [
            {
                "icon": "volume_off",
                "title": "전기음/기계음 잡음",
                "problem": "현장 50/60Hz 전기 험 → 모델 오분류",
                "action": "Welch PSD + Notch 필터 자동 제거",
                "result": "전처리 품질 향상, 오분류율 감소",
                "color": "#ef4444",
            },
            {
                "icon": "fork_right",
                "title": "Multi-class 전환 시 성능 저하",
                "problem": "2클래스 → 3클래스 전환 시 H 오분류 증가",
                "action": "데이터셋 재구성 + 교차 검증 비교",
                "result": "V8-2-1 운영 적용 (Val Acc 91.44%)",
                "color": "#f59e0b",
            },
            {
                "icon": "public",
                "title": "지역별 데이터 편차",
                "problem": "한국 학습 모델 → 인도네시아 성능 저하",
                "action": "글로벌 테스트셋 + Folium 시각화",
                "result": "지역별 편차 정량 파악, 적응형 기반 마련",
                "color": "#8b5cf6",
            },
        ],

        # ── 5. Impact & Retrospective ──
        "results": [
            {"value": "91.44%", "label": "Best Val Accuracy", "sub": "V8-2-1 운영 모델"},
            {"value": "2,801", "label": "학습 샘플", "sub": "Train 1,960 / Val 841"},
            {"value": "91.64%", "label": "Best Val F1", "sub": "Precision·Recall 균형"},
            {"value": "8개국", "label": "글로벌 배포", "sub": "KR, ID, MY, TH, TR, IN, VN, US"},
        ],
        "model_evolution": [
            {"version": "V8-2-1", "type": "Multi-class", "classes": "L / H / N", "model": "Custom CNN", "accuracy": 91.44, "production": True, "note": "운영 적용 모델"},
            {"version": "V8-2-2", "type": "Multi-class", "classes": "L / H / N", "model": "Custom CNN", "accuracy": 89.18, "production": False, "note": "데이터셋 변형 실험"},
            {"version": "V8-2-3", "type": "Multi-class", "classes": "L / H / LH / N", "model": "Custom CNN", "accuracy": 88.82, "production": False, "note": "4클래스 확장"},
        ],
        "model_comparison_note": "각 모델의 Validation Dataset을 MinIO에서 교차 조회하여 동일 조건에서 공정 비교 수행",
        "lessons": [
            "도메인 지식(음향 신호처리)이 모델 성능을 크게 좌우함을 체감 — 전처리 품질이 아키텍처만큼 중요",
            "데이터 거버넌스(버전 관리, 라벨 정합성)가 반복 고도화의 전제 조건",
            "MLflow 기반 실험 관리가 '감'이 아닌 '데이터'로 의사결정하는 문화를 정착시킴",
        ],
    },
    {
        "id": "komipo-zeroleak",
        "title": "발전소 누수 진단 IoT 서비스",
        "subtitle": "KOMIPO ZeroLeak - Power Plant Leak Detection",
        "color": "#ef4444",
        "icon": "factory",
        "period": "2025.05 ~ 현재",
        "team": "BE 2 / FE 1 / AI 1",
        "contribution": "AI 기여도 100%",

        # ── Screenshots ──
        "screenshots": [
            {"src": "/static/images/komipo_dashboard.png", "caption": "AI 스마트 누수 관리 시스템 - 대시보드"},
            {"src": "/static/images/komipo_leak_monitoring.png", "caption": "음수집 누수음 모니터링"},
            {"src": "/static/images/komipo_pressure.png", "caption": "압력 모니터링"},
        ],

        # ── 1. Project Overview ──
        "summary": "발전소 내 소화전·밸브 배관에 IoT 음수집 센서를 부착하여 수집한 음향 데이터를 Autoencoder 이상탐지 모델로 분석, 고소음 산업 환경에서의 누수를 자동 진단하는 시스템",
        "role": "AI 모델 E2E 개발 (노이즈 분석/제거 → 특징 추출 → Autoencoder 설계/학습 → 롤링 재학습 → 웹 서비스 배포)",
        "tech_stack": {
            "AI/ML": ["TensorFlow", "Keras", "Autoencoder", "Isolation Forest"],
            "Signal": ["LibROSA", "SciPy", "noisereduce", "FFT/STFT"],
            "Backend": ["Flask", "NestJS", "Express", "Nginx", "Docker"],
            "Data": ["MySQL", "SFTP", "Pandas", "NumPy"],
        },
        "metrics": [
            {"value": "26", "label": "모니터링 포인트"},
            {"value": "1,519", "label": "특징 차원"},
            {"value": "4주", "label": "롤링 재학습 주기"},
            {"value": "95th", "label": "이상탐지 임계값"},
        ],

        # ── 2. Background & Objective ──
        "background": {
            "pain_points": [
                "발전소 내부는 60Hz 전기음, 펌프·컴프레서 기계음 등 고소음 환경",
                "기존 일반 누수 탐지 모델(NELOW)을 그대로 적용 시 소음을 누수로 오분류",
                "계절·가동 상태에 따라 소음 패턴이 변화하여 고정 모델로는 대응 불가",
            ],
            "goals": [
                "발전소 특화 노이즈 제거 파이프라인 구축 (전기음·기계음 분리 제거)",
                "26개 모니터링 포인트별 개별 Autoencoder 모델 학습·운영",
                "4주 롤링 윈도우 자동 재학습으로 환경 변화에 적응",
            ],
            "before": [
                {"step": "수동 현장 점검", "icon": "person_search"},
                {"step": "고소음으로\n청음 판별 불가", "icon": "volume_off"},
                {"step": "일반 모델\n오분류 다수", "icon": "error_outline"},
                {"step": "비효율적 유지보수", "icon": "trending_down"},
            ],
            "after": [
                {"step": "소화전·밸브에\nIoT 센서 부착", "icon": "sensors"},
                {"step": "발전소 특화\n노이즈 제거", "icon": "tune"},
                {"step": "Autoencoder\n이상탐지", "icon": "psychology"},
                {"step": "실시간 자동 진단", "icon": "trending_up"},
            ],
        },

        # ── 3. Core Strategy & Implementation ──
        "pipeline_steps": [
            {"icon": "sensors", "label": "WAV 수집", "sub": "소화전·밸브 센서", "color": "#ef4444"},
            {"icon": "speed", "label": "8kHz 리샘플링", "sub": "표준화", "color": "#64748b"},
            {"icon": "content_cut", "label": "1초 추출", "sub": "최소 에너지 구간", "color": "#64748b"},
            {"icon": "volume_off", "label": "노이즈 제거", "sub": "전기음·기계음", "color": "#f59e0b"},
            {"icon": "graphic_eq", "label": "1519D 특징 추출", "sub": "Freq+Spectral+MFCC", "color": "#8b5cf6"},
            {"icon": "psychology", "label": "Autoencoder", "sub": "1519→32→1519", "color": "#3b82f6"},
            {"icon": "verified", "label": "이상탐지", "sub": "MSE > 95th %ile", "color": "#10b981"},
        ],
        "preprocess_steps": [
            {"label": "원본 WAV", "sub": "발전소 소화전·밸브 IoT 센서 수집", "color": "#64748b"},
            {"label": "8kHz 리샘플링", "sub": "표준 샘플레이트로 통일", "color": "#64748b"},
            {"label": "최소 표준편차 1초 구간 선택", "sub": "0.1초 윈도우 분할 → 안정적인 1초 구간 자동 선택", "color": "#06b6d4"},
            {"label": "Welch PSD 전기음 탐지 + Notch 필터", "sub": "60Hz 기본파 + 고조파 자동 감지·제거", "color": "#ef4444", "branch": True},
            {"label": "noisereduce 기계음 제거", "sub": "스펙트럼 차감 기반 배경 소음 제거", "color": "#ef4444", "branch": True},
            {"label": "1519D 특징 벡터 추출", "sub": "Frequency 1501 + Spectral 5 + MFCC 13", "color": "#10b981"},
        ],

        "architecture_mermaid": "",
        "preprocessing_mermaid": "",

        "technical_choices": [
            {"choice": "Autoencoder 이상탐지", "reason": "정상 데이터만으로 학습 가능, 라벨링 불필요 — 누수 사례가 희소한 산업 환경에 적합"},
            {"choice": "1519차원 특징 벡터", "reason": "주파수 1501 + 스펙트럼 5 + MFCC 13 — 누수 음향의 다면적 특성 포착"},
            {"choice": "95th %ile 임계값", "reason": "데이터 분포 기반 적응형 기준선, 지역별 자동 보정"},
            {"choice": "4주 롤링 재학습", "reason": "계절·가동 변화에 적응, 펌프 사이클 ≤3회/주인 정상 구간만 학습"},
            {"choice": "Welch PSD + Notch 필터", "reason": "60Hz 전기음과 고조파를 자동 감지·제거"},
            {"choice": "Flask + NestJS 마이크로서비스", "reason": "AI 추론(Flask)과 디바이스 통신(NestJS) 분리, 독립 스케일링"},
        ],

        "cnn_architecture": [
            {"layer": "Input", "output": "(1,519)", "detail": "Freq 1501 + Spectral 5 + MFCC 13"},
            {"layer": "Dense(512) + ReLU + BN + Dropout", "output": "(512)", "detail": "Encoder Layer 1"},
            {"layer": "Dense(256) + ReLU + BN + Dropout", "output": "(256)", "detail": "Encoder Layer 2"},
            {"layer": "Dense(128) + ReLU + BN + Dropout", "output": "(128)", "detail": "Encoder Layer 3"},
            {"layer": "Dense(64) + ReLU + BN + Dropout", "output": "(64)", "detail": "Encoder Layer 4"},
            {"layer": "Dense(32) + ReLU", "output": "(32)", "detail": "Latent Space"},
            {"layer": "Dense(64→128→256→512) + ReLU", "output": "(512)", "detail": "Decoder (대칭)"},
            {"layer": "Dense(1519) + Linear", "output": "(1,519)", "detail": "Reconstruction Output"},
        ],

        "key_works": [
            {
                "title": "발전소 노이즈 제거 파이프라인",
                "icon": "volume_off",
                "color": "#ef4444",
                "desc": "전기음·기계음 자동 분리 제거",
                "tags": ["Welch PSD", "Notch Filter", "noisereduce", "60Hz 고조파"],
            },
            {
                "title": "26개 포인트별 Autoencoder",
                "icon": "hub",
                "color": "#f59e0b",
                "desc": "지역별 독립 모델 학습·배포",
                "tags": ["FH102~118", "V102~111", "95th %ile", "MSE 이상탐지"],
            },
            {
                "title": "웹 서비스 & 롤링 재학습",
                "icon": "cloud_sync",
                "color": "#8b5cf6",
                "desc": "4주 주기 자동 재학습 + API 서빙",
                "tags": ["Flask API", "NestJS", "Docker", "4주 Rolling"],
            },
        ],

        # ── 4. Obstacles & Troubleshooting ──
        "challenges": [
            {
                "icon": "electric_bolt",
                "title": "60Hz 전기음 + 고조파 잡음",
                "problem": "발전소 전기음이 누수 주파수 대역과 겹침",
                "action": "Welch PSD 고조파 탐지 + Notch 필터 자동 제거",
                "result": "전기음 분리 제거, 오분류율 대폭 감소",
                "color": "#ef4444",
            },
            {
                "icon": "water",
                "title": "펌프 사이클과 누수 신호 혼동",
                "problem": "펌프 가동 시 압력 변화가 누수 패턴과 유사",
                "action": "수압 FFT 분석으로 주간 펌프 사이클 ≤3회 정상 구간 필터링",
                "result": "정상 데이터 품질 확보, 학습 안정성 향상",
                "color": "#f59e0b",
            },
            {
                "icon": "update",
                "title": "계절·가동 상태 변화 대응",
                "problem": "고정 모델이 환경 변화에 적응하지 못해 성능 저하",
                "action": "4주 롤링 윈도우 재학습 + 적응형 95th %ile 임계값",
                "result": "환경 변화에 자동 적응하는 지속 운영 체계 구축",
                "color": "#8b5cf6",
            },
        ],

        # ── 5. Impact & Retrospective ──
        "results": [
            {"value": "26", "label": "모니터링 포인트", "sub": "소화전 17 + 밸브 10"},
            {"value": "1,519D", "label": "특징 벡터", "sub": "Freq + Spectral + MFCC"},
            {"value": "4주", "label": "롤링 재학습", "sub": "펌프 사이클 기반 필터링"},
            {"value": "24/7", "label": "실시간 운영", "sub": "Flask + NestJS + Docker"},
        ],
        "model_evolution": [
            {"version": "Autoencoder", "type": "이상탐지", "classes": "Normal vs Anomaly", "model": "AE (1519→32→1519)", "accuracy": 95, "production": True, "note": "운영 적용"},
        ],
        "model_comparison_note": "Autoencoder MSE 기반 95th percentile 임계값으로 이상탐지, 26개 포인트별 독립 모델 운영",
        "lessons": [
            "산업 현장의 도메인 노이즈 이해가 모델 성능의 핵심 — 전처리가 모델보다 중요할 수 있음",
            "롤링 재학습 체계가 '한번 배포하고 끝'이 아닌 지속 운영 가능한 AI 서비스의 기반",
            "마이크로서비스(Flask/NestJS/Express) 분리가 AI 모델 독립 업데이트를 가능하게 함",
        ],
    },
    {
        "id": "nelow-dashboard",
        "title": "글로벌 IoT 통신 상태 대시보드",
        "subtitle": "NELOW Global Device Monitoring Dashboard",
        "color": "#10b981",
        "icon": "dashboard",
        "period": "2025 ~ 현재",
        "team": "AI 1 (풀스택 단독 개발)",
        "contribution": "기여도 100%",

        # ── Screenshots ──
        "screenshots": [
            {"src": "/static/images/dashboard_main.png", "caption": "글로벌 IoT 통신 상태 대시보드 — 한국 고객사별 장비 현황"},
        ],

        # ── 1. Project Overview ──
        "summary": "8개국에 배포된 자사 IoT 장비(누수음·수압 센서)의 통신 상태를 실시간 모니터링하는 대시보드. 각국 고객사별 장비 수신율을 자동 집계하여 이상 장비를 즉시 파악할 수 있는 운영 관리 시스템",
        "role": "풀스택 단독 개발 (FastAPI 백엔드 + Vue 3 프론트엔드 + Prefect 배치 + Docker 배포)",
        "tech_stack": {
            "Frontend": ["Vue 3", "TypeScript", "Tailwind CSS", "Leaflet", "ECharts"],
            "Backend": ["FastAPI", "asyncpg", "PostgreSQL"],
            "Batch": ["Prefect", "pymysql", "Circuit Breaker"],
            "Infra": ["Docker Compose", "Nginx", "8x MariaDB"],
        },
        "metrics": [
            {"value": "8개국", "label": "모니터링 국가"},
            {"value": "2종", "label": "장비 유형 (누수음/수압)"},
            {"value": "1시간", "label": "배치 집계 주기"},
            {"value": "5분", "label": "대시보드 자동 갱신"},
        ],

        # ── 2. Background & Objective ──
        "background": {
            "pain_points": [
                "8개국 고객사에 배포된 IoT 장비의 통신 상태를 개별적으로 파악해야 하는 비효율",
                "장비 통신 이상을 고객 클레임 이후에야 인지 — 선제 대응 불가",
                "국가별 DB가 분산되어 있어 통합 모니터링 체계 부재",
            ],
            "goals": [
                "8개국 IoT 장비 통신 상태를 단일 대시보드에서 실시간 통합 모니터링",
                "장비 수신율 기반 자동 이상 판별 (정상/주의/이상) — 선제 대응 가능",
                "혁신사업부에서 어느 고객사의 장비에 이상이 있는지 즉시 파악",
            ],
            "before": [
                {"step": "국가별 DB\n개별 조회", "icon": "storage"},
                {"step": "수동 확인\n누락 발생", "icon": "search"},
                {"step": "고객 클레임 후\n인지", "icon": "warning"},
                {"step": "대응 지연", "icon": "trending_down"},
            ],
            "after": [
                {"step": "8개국 DB\n자동 집계", "icon": "sync"},
                {"step": "지도 기반\n실시간 현황", "icon": "map"},
                {"step": "이상 장비\n즉시 알림", "icon": "notifications_active"},
                {"step": "선제 대응", "icon": "trending_up"},
            ],
        },

        # ── 3. Core Strategy & Implementation ──
        "pipeline_steps": [
            {"icon": "sensors", "label": "IoT 장비", "sub": "8개국 누수음·수압", "color": "#06b6d4"},
            {"icon": "storage", "label": "8x MariaDB", "sub": "국가별 분산 DB", "color": "#64748b"},
            {"icon": "schedule", "label": "Prefect 배치", "sub": "1시간 주기 집계", "color": "#f59e0b"},
            {"icon": "analytics", "label": "PostgreSQL", "sub": "통합 분석 DB", "color": "#8b5cf6"},
            {"icon": "api", "label": "FastAPI", "sub": "REST API 서빙", "color": "#3b82f6"},
            {"icon": "dashboard", "label": "Vue 3 대시보드", "sub": "Leaflet 지도 + ECharts", "color": "#10b981"},
        ],
        "preprocess_steps": [
            {"label": "8개국 MariaDB에서 장비별 수신 데이터 조회", "sub": "D-1, D-2, D-3 일별 수신 건수 확인", "color": "#64748b"},
            {"label": "수압 장비: 70% 수신율 기준 판별", "sub": "10분 간격 × 144회/일 → 100회 이상이면 정상", "color": "#06b6d4"},
            {"label": "누수음 장비: 3/3 수신 기준 판별", "sub": "일 3회 고정 → 3회 모두 수신이면 정상", "color": "#06b6d4"},
            {"label": "상태 판정: 정상/주의/이상/미확인", "sub": "D-1 OK → 정상 | D-1,2 없고 D-3 OK → 주의 | D-1,2,3 모두 없음 → 이상", "color": "#f59e0b"},
            {"label": "고객사 상태 집계", "sub": "이상 장비 30% 이상이면 고객사 이상 판정", "color": "#ef4444", "branch": True},
            {"label": "PostgreSQL에 일별 상태 적재", "sub": "device_status_log + customer_status_log UPSERT", "color": "#10b981"},
        ],

        "architecture_mermaid": "",
        "preprocessing_mermaid": "",

        "technical_choices": [
            {"choice": "Prefect 워크플로우", "reason": "Cron 배치 스케줄링 + 태스크 단위 에러 핸들링 + 수동 백필 지원"},
            {"choice": "Circuit Breaker 패턴", "reason": "국가별 DB 장애 시 연쇄 타임아웃 방지 (2회 실패 → 30분 차단)"},
            {"choice": "Watermark 기반 지연 도착 감지", "reason": "늦게 도착한 데이터도 과거 날짜 상태를 자동 재계산 (최대 365일)"},
            {"choice": "Leaflet + ECharts", "reason": "지도 기반 위치 시각화 + 수신율 바 차트 (30/60/365일)"},
            {"choice": "asyncpg 커넥션 풀", "reason": "PostgreSQL 비동기 접근으로 동시 API 요청 처리 성능 확보"},
            {"choice": "Docker Compose 4-서비스 구성", "reason": "Nginx / Backend / Frontend / Batch 독립 운영·스케일링"},
        ],

        "cnn_architecture": [
            {"layer": "Nginx (port 80)", "output": "Reverse Proxy", "detail": "Basic Auth + 라우팅 (/api → Backend, / → Frontend)"},
            {"layer": "FastAPI (port 8000)", "output": "REST API", "detail": "asyncpg 풀, 11개 엔드포인트"},
            {"layer": "Vue 3 (port 5174)", "output": "SPA", "detail": "Leaflet 지도 + ECharts + Pinia 상태관리"},
            {"layer": "Prefect Batch", "output": "Hourly Flow", "detail": "8개국 DB 조회 → 상태 판정 → PostgreSQL 적재"},
            {"layer": "PostgreSQL", "output": "Analytics DB", "detail": "device/customer_status_log, batch_watermark"},
            {"layer": "8x MariaDB", "output": "Regional DB", "detail": "KR, IN, TR, MY, VN, ID, TH, US"},
        ],

        "key_works": [
            {
                "title": "Prefect 배치 파이프라인",
                "icon": "schedule",
                "color": "#f59e0b",
                "desc": "1시간 주기 8개국 장비 상태 자동 집계",
                "tags": ["Prefect Flow", "Circuit Breaker", "Watermark", "Auto Backfill"],
            },
            {
                "title": "Vue 3 인터랙티브 대시보드",
                "icon": "map",
                "color": "#10b981",
                "desc": "지도 기반 3-depth 드릴다운 UI",
                "tags": ["Leaflet", "ECharts", "Pinia", "드래그 정렬"],
            },
            {
                "title": "FastAPI + PostgreSQL 백엔드",
                "icon": "api",
                "color": "#3b82f6",
                "desc": "비동기 API + 통합 분석 DB 설계",
                "tags": ["asyncpg", "UPSERT", "커넥션 풀", "11 endpoints"],
            },
        ],

        # ── 4. Obstacles & Troubleshooting ──
        "challenges": [
            {
                "icon": "cloud_off",
                "title": "국가별 DB 장애 시 연쇄 타임아웃",
                "problem": "한 국가 DB 다운 → 전체 배치 지연",
                "action": "Circuit Breaker 패턴 적용 (2회 실패 → 30분 차단)",
                "result": "장애 국가 격리, 나머지 정상 처리 보장",
                "color": "#ef4444",
            },
            {
                "icon": "schedule_send",
                "title": "IoT 데이터 지연 도착",
                "problem": "장비 데이터가 1~7일 늦게 DB에 반영되는 케이스",
                "action": "Watermark 기반 지연 감지 + 과거 날짜 자동 재계산",
                "result": "최대 365일 이전 데이터까지 자동 보정",
                "color": "#f59e0b",
            },
            {
                "icon": "sync_problem",
                "title": "배치 중단 시 데이터 공백",
                "problem": "서버 재시작 등으로 배치 미실행 → 대시보드 빈 날짜",
                "action": "Auto Gap Catch-up (최대 7일 자동 백필)",
                "result": "운영 중단 없는 연속적 모니터링 보장",
                "color": "#8b5cf6",
            },
        ],

        # ── 5. Impact & Retrospective ──
        "results": [
            {"value": "8개국", "label": "통합 모니터링", "sub": "KR, IN, TR, MY, VN, ID, TH, US"},
            {"value": "100%", "label": "단독 개발", "sub": "Frontend + Backend + Batch"},
            {"value": "24/7", "label": "실시간 운영", "sub": "1시간 배치 + 5분 갱신"},
            {"value": "혁신사업부", "label": "실 사용 부서", "sub": "장비 이상 선제 대응 활용"},
        ],
        "model_evolution": [],
        "model_comparison_note": "",
        "lessons": [
            "분산 DB 환경에서 Circuit Breaker·Watermark 같은 장애 내성 패턴이 안정적 운영의 핵심",
            "풀스택 단독 개발 경험으로 프론트엔드-백엔드-배치 간 데이터 흐름을 전체적으로 설계하는 역량 확보",
            "실 사용 부서(혁신사업부)의 피드백을 반영한 반복 개선이 서비스 정착의 핵심 요인",
        ],
    },
    {
        "id": "shinpyung-dqn",
        "title": "강화학습 기반 정수장 펌프 제어 최적화",
        "subtitle": "Shinpyung DQN - RL Pump Control Optimization",
        "color": "#8b5cf6",
        "icon": "psychology",
        "period": "2025 ~ 현재",
        "team": "AI Team",
        "contribution": "AI 기여도 100%",

        # ── Screenshots ──
        "screenshots": [
            {"src": "/static/images/dqn_sim_scenario.png", "caption": "시나리오 모드 — 실제 운영 데이터 재생"},
            {"src": "/static/images/dqn_sim_recommend.png", "caption": "DQN 추천 — AI 제어 행동 추천 + 예측"},
            {"src": "/static/images/dqn_sim_auto.png", "caption": "DQN 자동 — AI 자동 제어 시뮬레이션"},
        ],

        # ── 1. Project Overview ──
        "summary": "신평공업 가압장의 인버터 펌프(#4)를 Dueling DQN 강화학습으로 자동 제어하여, 수위 안전 범위를 유지하면서 시간대별 전력 요금을 고려한 전력비 절감을 목표로 하는 최적 제어 시스템",
        "role": "환경해석모델(Physics-informed NN) + Dueling DQN 에이전트 설계·학습 + MLflow 실험 관리 + 시뮬레이션 웹 UI",
        "tech_stack": {
            "RL/ML": ["PyTorch", "Dueling DQN", "Double DQN", "Replay Buffer"],
            "Env Model": ["Physics-informed NN", "Multi-task Learning", "ResidualBlock"],
            "Infra": ["MLflow", "MinIO(S3)", "FastAPI", "WebSocket"],
            "Data": ["Pandas", "scikit-learn", "MinMaxScaler"],
        },
        "metrics": [
            {"value": "14D", "label": "상태 공간"},
            {"value": "9", "label": "행동 공간"},
            {"value": "V8", "label": "환경모델 버전"},
            {"value": "27+", "label": "DQN Sweep 실험"},
        ],

        # ── 2. Background & Objective ──
        "background": {
            "pain_points": [
                "정수장 펌프 운전이 운전원의 경험에 의존 — 시간대별 전력 요금 최적화 미반영",
                "펌프 ON/OFF 빈도와 주파수 변경이 잦아 장비 수명 단축 우려",
                "수위(배수지·조절지·흡수정) 안전 범위를 유지하면서 전력비를 줄이는 최적점 탐색이 어려움",
            ],
            "goals": [
                "DQN 강화학습으로 시간대별 전력 요금(경부하/중부하/최대부하)을 고려한 최적 펌프 제어 정책 학습",
                "수위 안전 범위 유지 + 전력비 절감 + 장비 보호(펌프 변경 최소화) 다목적 최적화",
                "환경해석모델(NN')로 제어 행동의 결과를 예측하여 Model-based RL 학습 가능",
            ],
            "before": [
                {"step": "운전원\n경험 기반 제어", "icon": "person"},
                {"step": "전력 요금\n미고려", "icon": "payments"},
                {"step": "잦은 ON/OFF\n장비 마모", "icon": "warning"},
                {"step": "비효율 운영", "icon": "trending_down"},
            ],
            "after": [
                {"step": "DQN 에이전트\n자동 제어", "icon": "smart_toy"},
                {"step": "시간대별 요금\n최적화", "icon": "savings"},
                {"step": "안정적\n펌프 운전", "icon": "verified"},
                {"step": "전력비 절감", "icon": "trending_up"},
            ],
        },

        # ── 3. Core Strategy & Implementation ──
        "pipeline_steps": [
            {"icon": "sensors", "label": "실시간 센서", "sub": "수위·유량·전력 14D", "color": "#06b6d4"},
            {"icon": "analytics", "label": "환경해석모델", "sub": "NN' (22D→4D)", "color": "#f59e0b"},
            {"icon": "psychology", "label": "Dueling DQN", "sub": "Q-value 9 actions", "color": "#8b5cf6"},
            {"icon": "calculate", "label": "보상 계산", "sub": "전력비+수위+안정성", "color": "#ef4444"},
            {"icon": "tune", "label": "펌프 제어", "sub": "OFF or 47~54Hz", "color": "#10b981"},
        ],
        "preprocess_steps": [
            {"label": "14D 상태 관측", "sub": "펌프 상태(2) + 수위(5) + 시간(2) + 유량(3) + 전력(1) + 주파수(1)", "color": "#06b6d4"},
            {"label": "환경해석모델 예측 (22D→4D)", "sub": "현재 상태 + 1시간 Lag → 다음 시간 전력·수위 예측", "color": "#f59e0b"},
            {"label": "DQN 행동 선택 (9가지)", "sub": "펌프 OFF(1) + ON 47~54Hz(8) = 9 이산 행동", "color": "#8b5cf6"},
            {"label": "다목적 보상 함수 계산", "sub": "전력비 + 수위 페널티 + 펌프 변경 페널티 + 안정성 보너스", "color": "#ef4444", "branch": True},
            {"label": "시간대별 전력 요금 반영", "sub": "경부하 60원 | 중부하 100원 | 최대부하 150원/kWh", "color": "#f59e0b", "branch": True},
            {"label": "최적 제어 정책 업데이트", "sub": "ε-greedy 탐색 → Replay Buffer → Double DQN 학습", "color": "#10b981"},
        ],

        "architecture_mermaid": "",
        "preprocessing_mermaid": "",

        "technical_choices": [
            {"choice": "Dueling DQN + Double DQN", "reason": "Value/Advantage 분리로 일반화 성능 향상 + Q-value 과대추정 방지"},
            {"choice": "Physics-informed 환경모델", "reason": "전력을 Base Load + Pump 기여로 분해 — 물리적 해석 가능성 확보"},
            {"choice": "9 이산 행동 공간", "reason": "산업 현장 제약: 펌프 주파수 47~54Hz 정수 단위 + ON/OFF"},
            {"choice": "Multi-task Loss (전력 3.0 + 수위 1.5)", "reason": "전력 예측 정확도를 우선하되 수위 안전도 보장"},
            {"choice": "MLflow + Sweep 실험", "reason": "27+ 하이퍼파라미터 조합 체계적 탐색·비교"},
            {"choice": "Model-based RL", "reason": "환경모델로 행동→결과 예측, 실제 시설 운전 없이 학습 가능"},
        ],

        "cnn_architecture": [
            {"layer": "State Input", "output": "(14)", "detail": "수위·유량·전력·시간·펌프 상태"},
            {"layer": "Feature Net: Linear(256)+ReLU+LN ×2", "output": "(256)", "detail": "공유 특징 추출"},
            {"layer": "Value Stream: Linear(128)+ReLU → Linear(1)", "output": "(1)", "detail": "상태 가치 V(s)"},
            {"layer": "Advantage Stream: Linear(128)+ReLU → Linear(9)", "output": "(9)", "detail": "행동 이점 A(s,a)"},
            {"layer": "Q(s,a) = V(s) + A(s,a) - mean(A)", "output": "(9)", "detail": "최종 Q-value"},
        ],

        "key_works": [
            {
                "title": "Physics-informed 환경해석모델",
                "icon": "schema",
                "color": "#f59e0b",
                "desc": "전력 = Base Load + Pump 기여 분해",
                "tags": ["22D→4D", "ResidualBlock", "V1~V8 반복", "MSE 0.0012"],
            },
            {
                "title": "Dueling DQN 에이전트",
                "icon": "psychology",
                "color": "#8b5cf6",
                "desc": "Value/Advantage 분리 + Double DQN",
                "tags": ["14D State", "9 Actions", "ε-greedy", "27+ Sweep"],
            },
            {
                "title": "다목적 보상 함수 설계",
                "icon": "calculate",
                "color": "#ef4444",
                "desc": "전력비·수위·장비보호 균형 최적화",
                "tags": ["시간대별 요금", "수위 페널티", "펌프 변경 페널티", "V7 안정성 보너스"],
            },
        ],

        # ── 4. Obstacles & Troubleshooting ──
        "challenges": [
            {
                "icon": "electric_bolt",
                "title": "환경모델 전력 예측 정확도",
                "problem": "펌프 ON/OFF 시 전력 패턴이 비대칭 → 단일 Loss로 학습 부족",
                "action": "ON/OFF 분리 Loss(0.7:0.3) + pump_hidden 64→512 확장 + V1~V8 반복",
                "result": "환경모델 best_test_mse 0.0012 달성 (V6)",
                "color": "#ef4444",
            },
            {
                "icon": "tune",
                "title": "DQN 보상 함수 균형 조정",
                "problem": "전력비만 최적화하면 수위 위반, 수위만 중시하면 전력 낭비",
                "action": "7개 보상 컴포넌트 설계 + V6~V7 단계적 도입 + 27+ sweep 실험",
                "result": "전력비·수위·안정성 균형잡힌 최적 제어 정책 도출",
                "color": "#f59e0b",
            },
            {
                "icon": "data_object",
                "title": "센서 데이터 품질 이슈",
                "problem": "센서 통신 두절(0값), 비물리적 유량(펌프OFF+유량>0) 등",
                "action": "V4 클리닝 파이프라인 (물리 제약 검증 + 선형 보간 limit=2)",
                "result": "데이터 품질 개선, 환경모델 학습 안정성 향상",
                "color": "#8b5cf6",
            },
        ],

        # ── 5. Impact & Retrospective ──
        "results": [
            {"value": "V8", "label": "환경모델", "sub": "best MSE 0.0012"},
            {"value": "27+", "label": "DQN Sweep", "sub": "하이퍼파라미터 탐색"},
            {"value": "9", "label": "제어 행동", "sub": "OFF + 47~54Hz"},
            {"value": "3종", "label": "시간대 요금", "sub": "60/100/150 원/kWh"},
        ],
        "model_evolution": [
            {"version": "Env V3", "type": "환경모델", "classes": "22D→4D", "model": "Physics NN", "accuracy": 99.2, "production": False, "note": "22D 입력 도입"},
            {"version": "Env V6", "type": "환경모델", "classes": "22D→4D", "model": "Physics NN", "accuracy": 99.88, "production": True, "note": "best MSE 0.00122"},
            {"version": "Env V8", "type": "환경모델", "classes": "22D→4D", "model": "Physics NN (512h)", "accuracy": 99.84, "production": False, "note": "pump_hidden 512"},
        ],
        "model_comparison_note": "환경해석모델 V1~V8 반복 고도화 + DQN 27+ sweep 실험을 MLflow로 관리, Accuracy = 1 - test_mse 환산",
        "lessons": [
            "Physics-informed 아키텍처가 블랙박스 NN보다 적은 데이터로 더 정확한 산업 환경 예측을 가능하게 함",
            "보상 함수 설계가 RL 성능의 핵심 — 컴포넌트 분리 + 가중치 sweep이 효과적",
            "실제 산업 데이터의 센서 이상(0값, 비물리적 값)에 대한 도메인 기반 클리닝이 모델 성능 전제 조건",
        ],
    },
    {
        "id": "seonsan-simulation",
        "title": "선산가압장 수위 예측 시뮬레이터",
        "subtitle": "Seonsan Water Level Prediction & Q-table Simulator",
        "color": "#06b6d4",
        "icon": "waves",
        "period": "2025.03 ~ 현재",
        "team": "AI 1 (단독 개발)",
        "contribution": "AI 기여도 100%",

        # ── Screenshots ──
        "screenshots": [
            {"src": "/static/images/seonsan_simulation_chart.png", "caption": "신·구 배수지 수위 비교 차트 — 실측 vs V1/V2 시뮬레이션 vs 목표수위"},
            {"src": "/static/images/seonsan_simulation_decisions.png", "caption": "시간대별 결정 이력 — HOLD/RECOMMEND 판정 + Q-table 케이스 비교"},
            {"src": "/static/images/seonsan_simulation_stats.png", "caption": "통계 요약 — V1(가중합산) vs V2(가중RSS) 시뮬레이션 성능 비교"},
        ],

        # ── 1. Project Overview ──
        "summary": "선산가압장 신·구 배수지의 수위 예측 모델과 290개 Q-table 운전 케이스의 유효성을 검증하고, Q-value 가중치를 실시간 튜닝하여 적정 제어 파라미터를 탐색하는 시뮬레이션 검증 도구",
        "role": "데이터 전처리 → MLP 모델 설계·학습(V1~V3) → Q-table 시뮬레이션 엔진 → Streamlit UI 개발 → MLflow 실험 관리 → Docker 배포",
        "tech_stack": {
            "AI/ML": ["PyTorch", "MLP", "scikit-learn", "MinMaxScaler"],
            "Infra": ["MLflow", "MinIO(S3)", "Docker", "Streamlit"],
            "Data": ["Pandas", "NumPy", "Parquet", "openpyxl"],
            "DB": ["MySQL(EMS)", "SQLAlchemy", "pymysql"],
        },
        "metrics": [
            {"value": "0.067m", "label": "Best MAE (신)"},
            {"value": "0.063m", "label": "Best MAE (구)"},
            {"value": "290", "label": "Q-table 케이스"},
            {"value": "5년+", "label": "학습 데이터"},
        ],

        # ── 2. Background & Objective ──
        "background": {
            "pain_points": [
                "Q-table 290개 운전 케이스가 실제 수위 제어에 유효한지 검증할 수단이 없음",
                "Q-value 계산 시 신·구 배수지 가중치의 적정값을 찾을 근거 부재",
                "수위 예측 모델의 제어 추천이 목표수위를 실제로 유지하는지 확인 불가",
            ],
            "goals": [
                "290개 Q-table 케이스별 Q-value를 자동 계산하여 최소값 케이스 추천 메커니즘 검증",
                "가중치(tight/loose)·게이트·패널티 파라미터를 실시간 조절하여 적정값 탐색",
                "24시간 연속 시뮬레이션으로 수위 예측 기반 제어가 목표수위를 유지하는지 검증",
            ],
            "before": [
                {"step": "Q-table 케이스\n검증 수단 없음", "icon": "help_outline"},
                {"step": "가중치\n경험적 설정", "icon": "tune"},
                {"step": "수위 제어 효과\n확인 불가", "icon": "visibility_off"},
                {"step": "운영 근거 부족", "icon": "trending_down"},
            ],
            "after": [
                {"step": "케이스별\nQ-value 자동 평가", "icon": "calculate"},
                {"step": "파라미터\n실시간 튜닝", "icon": "tune"},
                {"step": "24h 시뮬레이션\n수위 검증", "icon": "verified"},
                {"step": "근거 기반 운영", "icon": "trending_up"},
            ],
        },

        # ── 3. Core Strategy & Implementation ──
        "pipeline_steps": [
            {"icon": "storage", "label": "데이터 수집", "sub": "Excel + CSV 5년+", "color": "#64748b"},
            {"icon": "tune", "label": "전처리", "sub": "센서 선택·Lag 구성", "color": "#f59e0b"},
            {"icon": "psychology", "label": "MLP 학습", "sub": "V1~V3 모델 진화", "color": "#8b5cf6"},
            {"icon": "science", "label": "MLflow 등록", "sub": "메트릭·아티팩트 추적", "color": "#3b82f6"},
            {"icon": "calculate", "label": "Q-table 평가", "sub": "290개 케이스 스코어링", "color": "#ef4444"},
            {"icon": "dashboard", "label": "Streamlit UI", "sub": "24h 연속 시뮬레이션", "color": "#06b6d4"},
        ],
        "preprocess_steps": [
            {"label": "Excel + CSV 병합", "sub": "2020-12~2024-01 Excel + 2024-03~2026-04 CSV → Parquet 캐시", "color": "#64748b"},
            {"label": "Effective Level 선택", "sub": "4개 수위 센서 중 Primary/Fallback 자동 선택 (≤2.0m 불량 판정)", "color": "#06b6d4"},
            {"label": "Lag Feature 구성 (6h window)", "sub": "유입·유출·수위·밸브·센서상태 × 6시간 = 30차원 입력", "color": "#f59e0b"},
            {"label": "MinMaxScaler 정규화", "sub": "Train set 기준 fit → Val/Test transform", "color": "#8b5cf6"},
            {"label": "EMS 목표수위 조회", "sub": "MySQL DB에서 시간대별 목표수위 조회 (Fallback: 평균 프로필)", "color": "#ef4444", "branch": True},
            {"label": "시계열 분할", "sub": "Train 70% / Val 15% / Test 15% (시간순 유지)", "color": "#10b981"},
        ],

        "architecture_mermaid": "",
        "preprocessing_mermaid": "",

        "technical_choices": [
            {"choice": "MLP (128→64→32→1)", "reason": "시계열 Lag feature를 Flatten 입력으로 구성, 빠른 학습·추론으로 실시간 시뮬레이션 적합"},
            {"choice": "Effective Level 센서 선택", "reason": "4개 수위 센서의 불량(≤2.0m)을 자동 감지하여 Primary/Fallback 전환"},
            {"choice": "Q-table + 펌프 전환 패널티", "reason": "290개 운전 케이스에서 펌프 동시 전환·급격한 Hz 변경을 패널티로 필터링"},
            {"choice": "V1(가중합산) vs V2(가중RSS)", "reason": "두 전략을 병렬 실행하여 신·구 배수지 균형 최적화 비교"},
            {"choice": "MLflow + MinIO", "reason": "V1~V3 모델 버전별 메트릭·아티팩트 추적, 최고 성능 모델 자동 등록"},
            {"choice": "EMS DB 연동 (MySQL)", "reason": "실제 운영 목표수위를 실시간 조회하여 시뮬레이션 정확도 향상"},
        ],

        "cnn_architecture": [
            {"layer": "Input", "output": "(30)", "detail": "5종 feature × 6h Lag window"},
            {"layer": "Linear(128) + ReLU + Dropout(0.1)", "output": "(128)", "detail": "1층 특징 추출"},
            {"layer": "Linear(64) + ReLU + Dropout(0.1)", "output": "(64)", "detail": "2층 특징 압축"},
            {"layer": "Linear(32) + ReLU + Dropout(0.1)", "output": "(32)", "detail": "3층 특징 압축"},
            {"layer": "Linear(1)", "output": "(1)", "detail": "t+1h 수위 예측"},
        ],

        "key_works": [
            {
                "title": "Q-table 케이스 검증 엔진",
                "icon": "calculate",
                "color": "#ef4444",
                "desc": "290개 케이스별 Q-value 계산 + 최소값 추천 검증",
                "tags": ["Q-value 최소 선택", "펌프 전환 패널티", "HOLD/RECOMMEND", "케이스 SKIP 판정"],
            },
            {
                "title": "가중치 실시간 튜닝 UI",
                "icon": "tune",
                "color": "#f59e0b",
                "desc": "tight/loose·게이트·패널티 파라미터 실시간 조절",
                "tags": ["V1 가중합산", "V2 가중RSS", "게이트 임계값", "SimParams"],
            },
            {
                "title": "24h 수위 제어 검증 시뮬레이션",
                "icon": "verified",
                "color": "#06b6d4",
                "desc": "예측→제어→피드백 롤링 + 실측 대조 검증",
                "tags": ["Rolling Loop", "V1/V2 병렬 비교", "운영한계 초과 통계", "실측 3-way 비교"],
            },
        ],

        # ── 4. Obstacles & Troubleshooting ──
        "challenges": [
            {
                "icon": "ssid_chart",
                "title": "Distribution Shift (V1 test 성능 저하)",
                "problem": "V1 test 구간(2023-07~2024-01)의 운영 패턴이 train과 상이",
                "action": "V2c TimeSeriesSplit 3-fold + V3 최신 CSV 전용 재학습",
                "result": "신배수지 MAE 0.139m → 0.067m (52% 개선)",
                "color": "#ef4444",
            },
            {
                "icon": "sensors_off",
                "title": "수위 센서 불량 데이터",
                "problem": "4개 센서 중 청소·배수 시 ≤2.0m 비정상값 혼입",
                "action": "Effective Level 로직으로 Primary/Fallback 자동 전환",
                "result": "센서 불량 행 자동 제거, 학습 데이터 품질 확보",
                "color": "#f59e0b",
            },
            {
                "icon": "swap_horiz",
                "title": "펌프 전환 시 시스템 충격",
                "problem": "2대 이상 동시 ON↔OFF 전환 시 배관 압력 급변",
                "action": "3단계 펌프 전환 패널티 규칙 + Hz 변경폭 제한",
                "result": "위험 케이스 자동 SKIP, 안전한 제어 추천만 제공",
                "color": "#8b5cf6",
            },
        ],

        # ── 5. Impact & Retrospective ──
        "results": [
            {"value": "0.067m", "label": "신배수지 MAE", "sub": "V3 모델 (52% 개선)"},
            {"value": "0.063m", "label": "구배수지 MAE", "sub": "V3 모델 (R² 0.805)"},
            {"value": "290", "label": "Q-table 케이스", "sub": "펌프·밸브 조합 평가"},
            {"value": "24h", "label": "연속 시뮬레이션", "sub": "V1/V2 전략 비교 + 실측 대조"},
        ],
        "model_evolution": [
            {"version": "V1", "type": "MLP", "classes": "30D→1D", "model": "MLP (128-64-32)", "accuracy": 86.1, "production": False, "note": "MAE 0.139m"},
            {"version": "V2c", "type": "MLP+K-fold", "classes": "30D→1D", "model": "MLP (128-64-32)", "accuracy": 92.4, "production": False, "note": "MAE 0.076m"},
            {"version": "V3", "type": "MLP", "classes": "30D→1D", "model": "MLP (128-64-32)", "accuracy": 93.3, "production": True, "note": "MAE 0.067m (운영 적용)"},
        ],
        "model_comparison_note": "수위 예측 정확도 = (1 − MAE / 운영범위) — 신배수지 기준, V3는 MAE 0.067m으로 V1 대비 52% 개선",
        "lessons": [
            "시뮬레이션 검증 도구가 있어야 Q-table 케이스의 유효성과 가중치 적정값을 데이터 기반으로 판단할 수 있음",
            "V1(가중합산)과 V2(가중RSS)를 병렬 비교하는 구조 덕분에 전략 간 트레이드오프를 정량적으로 확인 가능",
            "수위 예측 모델의 정확도가 시뮬레이션 신뢰성의 전제 — Distribution Shift 대응(V3)이 검증 품질을 직접 좌우함",
        ],
    },
    {
        "id": "nelow-agent",
        "title": "NELOW Multi-Agent AI 시스템",
        "subtitle": "LangGraph-based Water Pressure Management Agent",
        "color": "#6366f1",
        "icon": "hub",
        "period": "2026.01 ~ 현재",
        "team": "BE 1 / FE 1 / AI 2",
        "contribution": "AI 기여도 50%",

        # ── Screenshots ──
        "screenshots": [
            {"src": "/static/images/nelow_agent_cheongyang_map.png", "caption": "청양군 — 측정 지점 클러스터 + NELOW AI Agent 자연어 대화 패널"},
            {"src": "/static/images/nelow_agent_pressure_anomaly.png", "caption": "수압이상분석 — analyze_pressure_status Tool이 블록별 수압 이상 지점 탐지·응답"},
            {"src": "/static/images/nelow_agent_leak_suspicion.png", "caption": "누수의심구간분석 — analyze_leak_points Tool이 DP/P75 기준으로 의심 지점 지도·테이블 렌더링"},
            {"src": "/static/images/nelow_agent_point_relationship.png", "caption": "지점관계도 — get_customer_flow_relationship Tool이 전체 지점 이름·연결 관계 오버레이"},
            {"src": "/static/images/nelow_agent_multi_chart.png", "caption": "멀티 차트 — show_mnp_chart Tool이 복수 지점 수압 시계열 + 요약 테이블 렌더링"},
            {"src": "/static/images/nelow_agent_mnp_chart.png", "caption": "MNP 차트 — 단일 지점 MNP(Minimum Night Pressure) + 온도 바차트 + 범위/최댓값 요약"},
            {"src": "/static/images/nelow_agent_neo4j_schema.png", "caption": "Neo4j 그래프 스키마 — 8 Labels (M2Point·Block·Customer·PumpingStation·PRV·Reservoir·Branch·GISLayer) / 3 RelTypes (IN_BLOCK·FLOWS_TO·BELONGS_TO)"},
            {"src": "/static/images/nelow_agent_neo4j_block_graph.png", "caption": "청양 M2Point-Block 구조 — IN_BLOCK 관계로 측정 지점 40개가 블록(주황)에 소속된 그래프"},
            {"src": "/static/images/nelow_agent_neo4j_flows.png", "caption": "청양 FLOWS_TO 관망 — 펌프장(주황)·PRV(분홍)·M2Point(파랑)·저수지(빨강)를 잇는 수압 전파 관계도"},
        ],

        # ── 1. Project Overview ──
        "summary": "지점별 속성·공간 위치·임베딩을 Neo4j 지식그래프로 직접 설계·구축하고, 에이전트가 이 그래프를 참조해 상황에 맞는 Tool을 자동 선택·호출하여 누수를 분석하는 LangGraph 기반 Agent 시스템 — OpenAI GPT에 22개 커스텀 Tool을 등록하고 Neo4j·MariaDB 조회 결과를 stream_writer로 지도·차트·관계도에 실시간 렌더링",
        "role": "22개 Tool E2E 개발(Pydantic 스키마·비즈니스 로직·UI Command) → OpenAI API 연동 + LangGraph Agent 설계 → Middleware 체인 → SSE 스트리밍 API → Prefect ETL",
        "tech_stack": {
            "AI/Agent": ["LangChain v1", "LangGraph", "create_agent", "OpenAI GPT"],
            "Data": ["Neo4j (Graph)", "MariaDB", "PostgreSQL Checkpointer", "text-embedding-3-large"],
            "Infra": ["FastAPI SSE", "Prefect 3.0", "Docker Compose", "Langfuse"],
            "Frontend": ["Vue 2", "Nginx", "Custom UI Command 프로토콜"],
        },
        "metrics": [
            {"value": "22", "label": "Agent Tools"},
            {"value": "3,432+", "label": "Langfuse Traces"},
            {"value": "50%", "label": "LLM 호출 감소"},
            {"value": "2개국어", "label": "한/영 Neo4j"},
        ],

        # ── 2. Background & Objective ──
        "background": {
            "pain_points": [
                "지점 속성·위치·관망 흐름 관계가 RDB에 산재되어 'A지점과 흐름상 연결된 주변 지점의 누수 의심도' 같은 관계형 질의를 LLM이 직접 답할 수 없었음",
                "'청양7블럭 누수 분석해줘' 같은 자연어 질의에 답하려면 LLM이 그래프 맥락을 근거로 상황에 맞는 도구를 직접 호출할 수 있어야 함",
                "LLM이 텍스트만 반환해서는 안되고, 지도·차트·관계도를 웹 UI에 실시간 렌더링해야 함",
            ],
            "goals": [
                "지점 속성·공간 위치·흐름 관계를 Neo4j 지식그래프로 직접 설계·구축하여 에이전트 Tool 호출의 근거로 활용",
                "OpenAI GPT + LangChain create_agent로 Tool-calling 기반 Agent 구축",
                "수압·누수·관계도 분석 로직을 22개 Tool로 직접 구현하여 LLM에 등록",
                "stream_writer + SSE 프로토콜로 Tool 실행 중 UI Command를 웹에 실시간 전송",
            ],
            "before": [
                {"step": "분산 DB\n수동 조회", "icon": "storage"},
                {"step": "대시보드만\n사용 가능", "icon": "dashboard"},
                {"step": "LLM 응답\n텍스트만", "icon": "text_snippet"},
                {"step": "분석 재현성\n낮음", "icon": "trending_down"},
            ],
            "after": [
                {"step": "자연어 질의\n한 번에 해결", "icon": "chat"},
                {"step": "22개 Custom Tool\nLLM 자동 호출", "icon": "build"},
                {"step": "지도·차트·관계도\n실시간 렌더링", "icon": "bolt"},
                {"step": "Tool 기반\n재현 가능 분석", "icon": "trending_up"},
            ],
        },

        # ── 3. Core Strategy & Implementation ──
        "pipeline_steps": [
            {"icon": "chat", "label": "자연어 질의", "sub": "SSE 스트리밍", "color": "#06b6d4"},
            {"icon": "psychology", "label": "NELOW Agent", "sub": "create_agent", "color": "#6366f1"},
            {"icon": "build", "label": "22개 Tool", "sub": "Query·Analysis·Display", "color": "#f59e0b"},
            {"icon": "hub", "label": "Neo4j 그래프", "sub": "구조·관계 데이터", "color": "#8b5cf6"},
            {"icon": "storage", "label": "MariaDB", "sub": "시계열·통계", "color": "#3b82f6"},
            {"icon": "stream", "label": "UI Command", "sub": "stream_writer", "color": "#ef4444"},
            {"icon": "dashboard", "label": "Vue Frontend", "sub": "지도·차트·관계도", "color": "#10b981"},
        ],
        "preprocess_steps": [
            {"label": "Prefect ETL (매일 04:00)", "sub": "MariaDB → Neo4j 동기화 플로우 (고객사별 필터링 지원)", "color": "#f59e0b"},
            {"label": "마스터 데이터 → Neo4j 지식그래프", "sub": "M2Point(위경도+POINT 공간타입+facility_type+embedding) · Block · Facility(PumpingStation/PRV/Reservoir) 노드 + IN_BLOCK/FLOWS_TO/BELONGS_TO 관계로 지점 속성·위치·관망 흐름을 1st-class 그래프로 승격", "color": "#8b5cf6"},
            {"label": "시계열 데이터 → MariaDB 유지", "sub": "MNP·수압·누수 측정값은 원본 DB에서 Analysis Tool이 직접 조회", "color": "#3b82f6"},
            {"label": "임베딩 생성 (text-embedding-3-large)", "sub": "포인트명·블록명 3072차원 벡터 → Neo4j Vector Index", "color": "#06b6d4"},
            {"label": "한/영 Neo4j 분리 인스턴스", "sub": "한국어(7687) / 영어(7689) 별도 동기화, 2개국어 지원", "color": "#ec4899", "branch": True},
            {"label": "PostgreSQL Checkpointer", "sub": "thread_id 기반 멀티턴 대화 상태 영구 저장", "color": "#10b981"},
        ],

        "architecture_mermaid": "",
        "preprocessing_mermaid": "",

        "technical_choices": [
            {"choice": "OpenAI GPT + ChatOpenAI", "reason": "temperature=0·streaming=True로 결정론적 응답 + SSE 토큰 스트리밍, with_structured_output으로 블록명 매칭 같은 Pydantic 스키마 응답 보장"},
            {"choice": "@tool + Pydantic args_schema", "reason": "각 Tool에 Field(description=...)로 파라미터 의미를 LLM에 전달, docstring으로 사용 조건(⚠️ 마크) 명시해 Tool 선택 정확도 향상"},
            {"choice": "22개 Custom Tool E2E 개발", "reason": "Query 7 / Analysis 7 / Display 3 / Utility 2 / Flow 3 — DB 조회·통계·UI 렌더링 로직을 모두 직접 구현"},
            {"choice": "stream_writer + UI Command", "reason": "Tool 실행 중 `writer({type:'ui_command', action, payload})` 호출로 지도·차트를 SSE custom 이벤트로 웹에 실시간 전송"},
            {"choice": "Neo4j 지식그래프 스키마 직접 설계", "reason": "M2Point(공간 POINT + lat/lng + facility_type + embedding 3072D) · Block · Facility 노드와 IN_BLOCK/FLOWS_TO/BELONGS_TO 관계로 지점의 속성·위치·관망 흐름을 1st-class 그래프로 모델링 → Tool이 관계를 1홉으로 탐색"},
            {"choice": "P75 기준선 누수 분석", "reason": "ΔP = 당일 MNP − 최근 4~30일 P75 백분위 → 누수 발생 20~25일 지속 감지, 임계값 −0.5 bar"},
            {"choice": "AgentPromptMiddleware (YAML + 동적)", "reason": "고객사명·기준 날짜·권한(is_root)을 매 호출마다 시스템 프롬프트에 주입"},
            {"choice": "ReferenceDateGuard Middleware", "reason": "Frontend에서 기준 날짜 변경 시 이전 분석 메시지 자동 삭제 → 모델 혼란 방지"},
            {"choice": "ContextEditingMiddleware", "reason": "Tool 결과가 1000 토큰 초과 시 `[cleared]`로 대체(최근 2개 유지) → 토큰 비용 약 75% 절감"},
            {"choice": "Langfuse Observability", "reason": "OpenAI 호출·Tool 실행·UI Command를 트레이스로 추적 (3,432+ 운영 트레이스 축적)"},
        ],

        "cnn_architecture": [
            {"layer": "FastAPI /chat/stream (SSE)", "output": "Event Stream", "detail": "token · ui_command · tool_start 이벤트 병렬 송신"},
            {"layer": "ChatOpenAI(GPT, temperature=0)", "output": "Tool Call", "detail": "streaming=True + with_structured_output 활용"},
            {"layer": "LangGraph create_agent", "output": "State Graph", "detail": "tools=22개 + middleware + PostgreSQL Checkpointer"},
            {"layer": "Middleware Stack (6)", "output": "프롬프트/히스토리 제어", "detail": "AgentPrompt · ReferenceDateGuard · ContextEditing · TurnLimit · TrimMessages · ErrorHandler"},
            {"layer": "Query Tools (7)", "output": "Raw Data dict", "detail": "search_points / search_blocks / get_mnp_timeseries_bulk ..."},
            {"layer": "Analysis Tools (7)", "output": "Command + UI Cmd", "detail": "analyze_leak_points(P75 ΔP) · analyze_pressure_status ..."},
            {"layer": "Display + Flow (6)", "output": "UI Command", "detail": "show_mnp_chart · map-flow-relationship · map-show-all-points"},
            {"layer": "stream_writer", "output": "Custom Event", "detail": "get_stream_writer()로 Tool 실행 중 UI Command 송신"},
            {"layer": "Frontend (Vue)", "output": "지도·차트·관계도 렌더링", "detail": "SSE 수신 → Leaflet/ECharts/관망도 업데이트"},
        ],

        "key_works": [
            {
                "title": "지식그래프 E2E 구축 (지점 속성·위치·관계)",
                "icon": "hub",
                "color": "#8b5cf6",
                "desc": "Prefect ETL로 매일 MariaDB 마스터 데이터를 Neo4j 지식그래프로 변환·동기화",
                "tags": ["M2Point POINT 공간", "FLOWS_TO 관망", "embedding 3072D", "IN_BLOCK/BELONGS_TO"],
            },
            {
                "title": "22개 Custom Tool 직접 개발",
                "icon": "build",
                "color": "#f59e0b",
                "desc": "@tool + Pydantic 스키마 + docstring으로 LLM 호출 규칙 주입",
                "tags": ["args_schema", "Field description", "⚠️ 사용 조건", "RuntimeContext 주입"],
            },
            {
                "title": "OpenAI API Tool-Calling Agent",
                "icon": "psychology",
                "color": "#6366f1",
                "desc": "ChatOpenAI + create_agent로 LLM이 상황별 Tool 자동 선택",
                "tags": ["ChatOpenAI", "temperature=0", "with_structured_output", "streaming"],
            },
            {
                "title": "stream_writer 웹 UI 실시간 연동",
                "icon": "stream",
                "color": "#ef4444",
                "desc": "Tool 실행 중 UI Command를 SSE custom 이벤트로 송신",
                "tags": ["get_stream_writer", "ui_command", "popup-mnp-chart", "map-flow-relationship"],
            },
            {
                "title": "P75 기준선 누수 분석 Tool",
                "icon": "water_drop",
                "color": "#06b6d4",
                "desc": "ΔP = 당일 MNP − 최근 30일 P75로 20~25일 누수 지속 감지",
                "tags": ["P75 Percentile", "ΔP < −0.5bar", "Top 3 + 1-hop", "FLOWS_TO 관계도"],
            },
        ],

        # ── 4. Obstacles & Troubleshooting ──
        "challenges": [
            {
                "icon": "hub",
                "title": "지식그래프 근거한 Tool 선택·누수 전파 추적",
                "problem": "'○○블럭 누수 분석' 같은 관계형 질의를 RDB만으로는 지점-블록-흐름을 조인·추적하기 어려움",
                "action": "M2Point·Block·Facility를 노드로, IN_BLOCK·FLOWS_TO·BELONGS_TO를 관계로 Neo4j 지식그래프 직접 설계 → Tool이 블록 소속 지점·FLOWS_TO 1-hop으로 상류·하류 전파 경로를 즉시 조회",
                "result": "analyze_leak_points가 Top 3 의심 지점 + 1-hop 주변을 단일 그래프 쿼리로 확장, LLM이 그래프 맥락을 근거로 Tool 연쇄 호출",
                "color": "#8b5cf6",
            },
            {
                "icon": "psychology",
                "title": "LLM의 Tool 선택 정확도",
                "problem": "'수압 이상'·'누수'·'지점'·'블록' 유사어 입력 시 LLM이 잘못된 Tool 호출 (예: point 대신 block 조회)",
                "action": "각 Tool docstring에 ⚠️ 사용 조건 명시 + Pydantic Field(description)에 예시·반례 기재 + YAML 프롬프트에 도메인 용어 정의",
                "result": "유사 질의에서도 Tool 자동 선택 안정화, 실운영 3,432+ 트레이스 축적",
                "color": "#6366f1",
            },
            {
                "icon": "token",
                "title": "Tool 결과 대용량으로 인한 토큰 폭증",
                "problem": "search_points 같은 조회 Tool 결과가 2,500+ 토큰, 멀티턴 누적 시 컨텍스트 한도 초과",
                "action": "ContextEditingMiddleware로 1000 토큰 초과 Tool 결과를 `[cleared]`로 대체(최근 2개 유지) + TurnLimit 2턴",
                "result": "토큰 사용량 약 75% 절감 (24k → 6k), Tool 체이닝 안전성 유지",
                "color": "#f59e0b",
            },
            {
                "icon": "stream",
                "title": "LLM 응답과 UI 렌더링 동기화",
                "problem": "Tool이 데이터만 반환하면 웹에 차트·지도가 즉시 뜨지 않아 사용자 경험 단절",
                "action": "`get_stream_writer()`로 Tool 실행 중 `{type:'ui_command', action, payload}` 이벤트를 SSE custom 스트림에 직접 송신",
                "result": "토큰 스트리밍과 UI 렌더링이 병렬 진행, 분석 결과가 실시간으로 지도·차트에 반영",
                "color": "#ef4444",
            },
            {
                "icon": "event_busy",
                "title": "기준 날짜 변경 시 모델 혼란",
                "problem": "Frontend에서 분석 기준 날짜 전환 시 이전 턴 데이터와 현재 질의가 섞여 엉뚱한 응답 생성",
                "action": "ReferenceDateGuardMiddleware가 state에 last_reference_date 저장 → 변경 감지 시 RemoveMessage로 이전 히스토리 일괄 삭제",
                "result": "날짜 전환 후 첫 턴부터 깨끗한 컨텍스트로 정확한 분석 유지",
                "color": "#8b5cf6",
            },
        ],

        # ── 5. Impact & Retrospective ──
        "results": [
            {"value": "22", "label": "통합 Tool", "sub": "Query·Analysis·Display·Flow"},
            {"value": "3,432+", "label": "Langfuse 트레이스", "sub": "실운영 질의 누적"},
            {"value": "50%", "label": "LLM 비용·지연 감소", "sub": "v3.0 Single Agent"},
            {"value": "한/영", "label": "다국어 지원", "sub": "Neo4j 인스턴스 분리"},
        ],
        "model_evolution": [
            {"version": "v1.0", "type": "Supervisor+Sub", "classes": "3 Sub-Agents", "model": "Supervisor Pattern", "accuracy": 70.0, "production": False, "note": "Neo4j+Text2SQL+UI Sub-Agent"},
            {"version": "v2.0", "type": "Supervisor", "classes": "Neo4j Sub + Tools", "model": "Hybrid", "accuracy": 85.0, "production": False, "note": "Text2SQL → Analysis Tools"},
            {"version": "v3.0", "type": "Single Agent", "classes": "22 Tools", "model": "create_agent", "accuracy": 95.0, "production": True, "note": "고수준 Tool Single Agent (운영)"},
        ],
        "model_comparison_note": "아키텍처 진화 — Accuracy는 LLM 호출 효율·Tool 선택 정확도 기반 정성 평가. v3.0에서 LLM 호출 50% 감소 + 응답 지연 2s 단축 달성",
        "lessons": [
            "지점의 속성·공간 위치·관계를 RDB가 아닌 지식그래프 1st-class로 모델링해야 LLM이 'A블록 주변 누수' 같은 관계형 질의에 Tool 연쇄로 답할 수 있음",
            "LLM의 능력은 등록된 Tool의 설계 수준으로 귀결됨 — Pydantic 스키마·docstring·Field description이 Tool 선택 정확도를 좌우",
            "Tool 반환 형식을 'LLM용 요약 + UI용 Command' 이원화하면 토큰 비용은 줄이면서 사용자 경험은 풍부하게 만들 수 있음",
            "stream_writer 같은 측면 채널로 Tool과 Frontend를 직접 연결하면 LLM을 거치지 않고도 UI 상태를 실시간 갱신 가능",
            "Middleware 체인(프롬프트·날짜·토큰)으로 Agent의 행동을 제어하면 모델 교체에도 안정적인 운영 품질 유지",
        ],
    },
    # ========================================================================
    # 7. LLM 실험·검증 랩 (3종 통합)
    # ========================================================================
    {
        "id": "llm-lab",
        "title": "LLM 실험·검증 랩",
        "subtitle": "Local LLM · Agent Evaluation · Voice-to-Web",
        "color": "#ec4899",
        "icon": "auto_awesome",
        "period": "2025.07 ~ 2026.01",
        "team": "AI 1",
        "contribution": "AI 기여도 100%",

        "screenshots": [],

        "summary": "LLM 활용 폭을 넓히기 위한 3종 실험 — Qwen3.5 122B 로컬 vLLM 서빙 + NELOW Agent Langfuse 자동 평가(50케이스 E2E 100%) + Whisper/GPT-4o/Playwright 기반 자사 웹 음성 조작 에이전트를 직접 구현해 LLM 스택 전반을 검증",
        "role": "3개 실험 단독 개발 — vLLM 서빙·NVFP4 양자화 검증 / Langfuse Dataset·Trace 평가 파이프라인 / Whisper→GPT-4o→Playwright 음성 자동화",
        "tech_stack": {
            "Local LLM": ["vLLM", "Qwen3.5-122B-A10B", "NVFP4 양자화", "Docker NVIDIA"],
            "Evaluation": ["Langfuse Dataset", "SSE E2E", "MariaDB 검증", "Trajectory"],
            "Voice Agent": ["Whisper small", "OpenAI GPT-4o", "Playwright", "PyAudio"],
            "Observability": ["Langfuse Trace", "LangChain callback"],
        },
        "metrics": [
            {"value": "122B", "label": "Qwen3.5 파라미터"},
            {"value": "50/50", "label": "E2E 통과율"},
            {"value": "60+", "label": "음성 지역 매핑"},
            {"value": "3종", "label": "LLM 스택 실험"},
        ],

        "sub_projects": [
            # ── ① Qwen3.5-122B 로컬 LLM 서빙 ──────────────────────────
            {
                "name": "Qwen3.5-122B 로컬 LLM 서빙",
                "icon": "dns",
                "color": "#ec4899",
                "period": "2025.12",
                "tagline": "vLLM Docker로 Qwen3.5-122B-A10B-NVFP4를 로컬 기동, OpenAI 호환 API + Langfuse trace로 latency·처리량 측정",
                "location": "/home/wook/qwen3.5-122b-a10b-nvfp4-sehyo",
                "tech_chips": ["vLLM cu130-aarch64", "NVFP4/marlin", "65k ctx", "Langfuse 3.x"],
                "file_tree": [
                    {"icon": "settings_ethernet", "path": "vllm/docker-compose.yml",
                     "role": "vLLM 서빙 컨테이너 정의 (포트 8002, host network, GPU 전체 할당, healthcheck /health 30s)"},
                    {"icon": "cloud_download", "path": "vllm/download_model.sh",
                     "role": "tmux 세션에서 huggingface_hub snapshot_download로 NVFP4 체크포인트 다운로드"},
                    {"icon": "terminal", "path": "test_langchain.py",
                     "role": "LangChain ChatOpenAI + Langfuse CallbackHandler로 single invoke / parallel abatch(5) 벤치 수행"},
                    {"icon": "description", "path": "pyproject.toml · uv.lock",
                     "role": "Python 3.13 · langchain 1.2.10 / langchain-openai / langfuse 3.14 / python-dotenv"},
                ],
                "execution_flow": [
                    {"icon": "cloud_download", "step": "모델 다운로드",
                     "detail": "`bash vllm/download_model.sh` — tmux 세션(`download-qwen3.5-122b-nvfp4-sehyo`)에서 `Sehyo/Qwen3.5-122B-A10B-NVFP4` 체크포인트를 `~/.cache/huggingface`에 받음"},
                    {"icon": "play_arrow", "step": "vLLM 컨테이너 기동",
                     "detail": "`docker compose up` — `vllm/vllm-openai:cu130-nightly-aarch64` 이미지가 `vllm serve` 실행, OpenAI 호환 `/v1` 엔드포인트를 포트 8002에 노출"},
                    {"icon": "health_and_safety", "step": "헬스체크 통과 대기",
                     "detail": "`curl /health` 30초 주기 · `start_period: 600s`로 모델 로드 대기 (NVFP4 가중치 로드 ~10분)"},
                    {"icon": "code", "step": "LangChain 클라이언트 초기화",
                     "detail": "`ChatOpenAI(base_url=http://localhost:8002/v1, api_key='EMPTY', model='my-model')`에 `CallbackHandler(update_trace=True)` 주입"},
                    {"icon": "query_stats", "step": "Single / Parallel 벤치",
                     "detail": "`run_single()`은 `invoke()` 단일 latency, `run_parallel()`은 `abatch([...]*5)` 병렬 처리량 측정 — 긴 가사 프롬프트 + 질의 2건으로 품질까지 확인"},
                    {"icon": "verified", "step": "Langfuse UI 확인",
                     "detail": "`langfuse.get_client().flush()` 후 Langfuse 대시보드의 Traces 탭에서 입출력 토큰·응답시간·에러를 통합 조회"},
                ],
                "key_configs": [
                    {"key": "이미지", "value": "vllm/vllm-openai:cu130-nightly-aarch64 (ARM64 + CUDA 13.0 nightly)"},
                    {"key": "모델", "value": "Sehyo/Qwen3.5-122B-A10B-NVFP4 (사전 양자화 체크포인트)"},
                    {"key": "vllm serve 인자", "value": "--max-model-len 65536 · --gpu-memory-utilization 0.7 · --max-num-seqs 100 · --max-num-batched-tokens 8192 · --enable-prefix-caching"},
                    {"key": "Tool-Calling 설정", "value": "--enable-auto-tool-choice · --tool-call-parser qwen3_coder · --reasoning-parser qwen3"},
                    {"key": "양자화 백엔드", "value": "VLLM_NVFP4_GEMM_BACKEND=marlin · VLLM_TEST_FORCE_FP8_MARLIN=1"},
                    {"key": "볼륨", "value": "~/.cache/huggingface · ~/.cache/vllm 마운트 (모델 재시작 시 재다운로드 방지)"},
                ],
                "highlight": "단일 노드 GPU에서 122B 파라미터 모델을 OpenAI 호환 API로 상시 서빙 + Langfuse로 로컬/클라우드 LLM을 동일 계측 체계로 비교",
            },

            # ── ② NELOW Agent Langfuse 평가 파이프라인 ───────────────────
            {
                "name": "NELOW Agent Langfuse 평가 파이프라인",
                "icon": "verified",
                "color": "#6366f1",
                "period": "2026.01",
                "tagline": "Langfuse Dataset(CSV) → Agent SSE 호출 → Tool·UI·E2E·Trajectory 4축 자동 채점",
                "location": "/root/nelow-agent/evaluate (운영서버 100.89.211.103)",
                "tech_chips": ["Langfuse Dataset", "SSE 스트림 파싱", "MariaDB 역검증", "Trajectory 비교"],
                "file_tree": [
                    {"icon": "settings_suggest", "path": "run_langfuse_tests_e2e.py",
                     "role": "평가 오케스트레이터 (~2400줄) — CSV 로드·SSE 호출·4축 검증·결과 집계"},
                    {"icon": "table_view", "path": "test_dataset_langfuse_{1,2,3,3-1,4}.csv",
                     "role": "152 케이스 데이터셋 (daily_mnp / leak_detection / block_mnp / point_anomaly_chart 등 카테고리)"},
                    {"icon": "schema", "path": "test_execution_flow.md",
                     "role": "5단계 테스트 플로우 mermaid 다이어그램 문서"},
                    {"icon": "folder", "path": "agent_evaluate_results/test_results_e2e_*.json",
                     "role": "회귀 실행 결과 JSON 아카이브 — 최종 50/50 통과 스냅샷 저장"},
                ],
                "execution_flow": [
                    {"icon": "file_open", "step": "CSV 데이터셋 로드",
                     "detail": "각 케이스에서 `input` · `expected_output` · `metadata(expected_tools, expected_ui_commands, validation_points)` 추출"},
                    {"icon": "send", "step": "Agent SSE 호출",
                     "detail": "`POST /stream {message, customer_id=37(곡성)}` — Agent가 SSE로 `tool_calls · ui_command · message · trace` 이벤트 전송"},
                    {"icon": "filter_alt", "step": "SSE 이벤트 파싱",
                     "detail": "`tool_calls` → 실제 호출 Tool · `ui_command` → action + payload · `message` → 최종 응답 · `trace` → Langfuse trace_id 확보"},
                    {"icon": "fact_check", "step": "4축 검증",
                     "detail": "① Tool Match(기대 툴 호출 여부) ② UI Match(action 일치) ③ E2E(MariaDB에서 point_id·날짜·MNP 값 역조회해 정확도 채점) ④ Trajectory(Langfuse observations로 agent→tool→response 순서 비교)"},
                    {"icon": "storage", "step": "MariaDB 역검증",
                     "detail": "`verify_daily_mnp_data` · `verify_leak_detection_data` · `verify_point_anomaly_chart` 함수가 Agent의 분석 로직을 재구현해 ground truth 생성 (bar↔psi 단위 변환 포함)"},
                    {"icon": "save", "step": "결과 집계·저장",
                     "detail": "케이스별 `tools_match · ui_match · e2e_passed · trajectory_passed · passed` 플래그 + `elapsed_time` + trace_id를 JSON으로 timestamp 파일에 저장"},
                ],
                "key_configs": [
                    {"key": "고객사", "value": "customer_id=37 (곡성) — 실제 운영 데이터 대상"},
                    {"key": "평가 지표", "value": "tools_match · ui_match · e2e_passed · trajectory_passed · overall passed (모두 True여야 통과)"},
                    {"key": "Trajectory 매칭", "value": "UI Command는 Langfuse에 미기록되므로 agent(start) → tool* → agent(response) 순서만 비교"},
                    {"key": "카테고리별 기대 툴", "value": "daily_mnp→analyze_daily_mnp · leak_detection→analyze_leak_points · block_mnp→analyze_block_mnp · point_anomaly→analyze_point_anomaly_chart"},
                    {"key": "DB 허용오차", "value": "max(0.5 psi, DB 값의 1%) + Agent가 bar로 반환 시 자동 psi 변환(×14.5038)"},
                    {"key": "실행 CLI", "value": "python run_langfuse_tests_e2e.py [--csv ...] [--test-id N] [--category daily_mnp]"},
                ],
                "highlight": "최종 50케이스에서 Tool·UI·E2E 전부 50/50 통과 + Trajectory 50/50 — 프롬프트·Tool 리팩토링 시 즉시 회귀 감지되는 자동 채점 파이프라인 확보",
            },

            # ── ③ HI NELOW 음성 웹 조작 ──────────────────────────────────
            {
                "name": "HI NELOW — 음성 기반 웹 조작 에이전트",
                "icon": "mic",
                "color": "#10b981",
                "period": "2025.07",
                "tagline": "Whisper 트리거(\"하이\") → 명령 녹음 → GPT-4o가 selector 생성 → Playwright로 자사 웹 조작",
                "location": "/home/wook/AI/HI_NELOW",
                "tech_chips": ["Whisper small", "GPT-4o", "Playwright sync", "PyAudio / keyboard"],
                "file_tree": [
                    {"icon": "record_voice_over", "path": "trigger.py (149줄)",
                     "role": "PyAudio 마이크 → Whisper STT → '하이' 트리거 감지 → SpaceBar 대기 → 명령 녹음 → process_command 호출"},
                    {"icon": "smart_toy", "path": "nelow.py (521줄)",
                     "role": "Playwright 로그인 세션 + GPT-4o 프롬프트 생성 + 응답 정규식 파싱 + 규칙 기반 분기 + DOM 액션 실행"},
                    {"icon": "map", "path": "region_value_map.json",
                     "role": "60개 지역명(한글) ↔ `<select>` value 매핑 JSON (예: 위플랫→\"1\", 곡성→\"37\")"},
                    {"icon": "description", "path": "pyproject.toml · .env",
                     "role": "openai · openai-whisper · playwright · pyaudio · keyboard + OPENAI_API_KEY / ID / PASSWORD"},
                ],
                "execution_flow": [
                    {"icon": "settings_voice", "step": "트리거 리스닝",
                     "detail": "PyAudio(16kHz/mono)로 3초 단위 녹음 → Whisper `small` 모델 한국어 STT → 'TRIGGER_KEYWORD = \"하이\"' 포함 감지"},
                    {"icon": "login", "step": "Playwright 로그인 세션",
                     "detail": "`create_logged_in_session()` — Chromium headless=False/최대화로 기동 → `kr.neverlosewater.com` 자동 로그인 → `#sidebar` 대기"},
                    {"icon": "keyboard", "step": "명령 녹음",
                     "detail": "SpaceBar 누르면 `record_until_silence()` — 최대 15초 / 무음 임계값 500·3초 지속 시 자동 종료 → Whisper로 한국어 텍스트 추출"},
                    {"icon": "psychology", "step": "GPT-4o 프롬프트·응답 파싱",
                     "detail": "`build_prompt()`로 [사용자 명령 + 웹 요소 목록(selector·href 3종) + 한국어 순서→숫자 매핑] 구성 → GPT-4o `chat.completions` 호출 → 정규식으로 `REGION / ACTION click(\"selector\") / HREF / ROOM_INDEX` 추출"},
                    {"icon": "rule", "step": "규칙 기반 오버라이드",
                     "detail": "\"작업방\"/\"강도\"/\"주파수\"/\"재생\" 키워드는 LLM 응답을 덮어쓰고 고정 분기(정렬·오디오 재생) 실행 — LLM 환각 차단 + 토큰 절약"},
                    {"icon": "touch_app", "step": "DOM 액션 실행",
                     "detail": "`region_value_map.json`으로 지역명→value 변환 후 `page.select_option('select.item-select', value=...)` → `page.goto(base_url+href)` → 작업방 진입/오디오 재생/테이블 정렬까지 Playwright로 체이닝"},
                ],
                "key_configs": [
                    {"key": "트리거 키워드", "value": "'하이' (trigger.py L14, 부분 일치)"},
                    {"key": "무음 감지", "value": "SILENCE_THRESHOLD=500 · SILENCE_DURATION=3s · MAX_RECORD=15s · CHUNK=1024"},
                    {"key": "STT 모델", "value": "whisper.load_model('small') + transcribe(language='ko')"},
                    {"key": "LLM 호출", "value": "OpenAI `gpt-4o`, system prompt 없음, user 메시지 1개로 selector 직접 생성 요구"},
                    {"key": "응답 파싱", "value": "click\\(\"(.+?)\"\\) / REGION:\\s*(\\S+) / HREF:\\s*(\\S+) / ROOM_INDEX:\\s*(\\d+) 4개 정규식"},
                    {"key": "세션 유지", "value": "Playwright sync context에 Chromium 생성 후 프로세스 종료까지 재사용"},
                ],
                "highlight": "관리자 페이지 반복 조작(로그인·지역 전환·누수음 작업방 진입·정렬·재생)을 음성 한마디로 단축 — STT 오인식은 매핑 테이블로, LLM 환각은 규칙 기반 분기로 이중 방어",
            },
        ],

        "results": [
            {"value": "122B", "label": "Qwen3.5 서빙", "sub": "NVFP4 / 65k ctx"},
            {"value": "50/50", "label": "E2E 통과", "sub": "Tool·UI·Data 전부"},
            {"value": "152", "label": "평가 케이스", "sub": "4개 CSV 데이터셋"},
            {"value": "60+", "label": "음성 지역", "sub": "관리자 페이지 매핑"},
        ],

        "lessons": [
            "로컬 LLM은 모델 크기보다 양자화·GEMM 백엔드 선택이 실사용 가능성을 좌우 — NVFP4+marlin 조합으로 122B도 단일 노드 서빙 가능",
            "Agent는 Langfuse Dataset + Trace observations로 Trajectory까지 자동 채점해야 프롬프트·Tool 리팩토링이 안전해짐",
            "음성 UX는 STT 품질이 아니라 '후처리 매핑 테이블'과 '규칙 기반 스킵'의 설계로 결정됨 — LLM을 모든 단계에 쓰지 않는 판단이 중요",
        ],
    },
]
