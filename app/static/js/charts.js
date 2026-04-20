document.addEventListener('DOMContentLoaded', () => {
    if (typeof skillsData === 'undefined') return;

    const darkTheme = {
        text: '#94a3b8',
        line: 'rgba(255,255,255,0.06)',
        blue: '#3b82f6',
        cyan: '#06b6d4',
        purple: '#8b5cf6',
        green: '#10b981',
        yellow: '#f59e0b',
    };

    // ─── Radar Chart ───
    const radarEl = document.getElementById('radar-chart');
    if (radarEl) {
        const radarChart = echarts.init(radarEl);
        radarChart.setOption({
            radar: {
                indicator: skillsData.map(s => ({ name: s.name, max: 100 })),
                shape: 'polygon',
                splitNumber: 4,
                axisName: { color: darkTheme.text, fontSize: 12, fontFamily: 'Pretendard, Inter, sans-serif' },
                splitLine: { lineStyle: { color: darkTheme.line } },
                splitArea: {
                    show: true,
                    areaStyle: { color: ['rgba(59,130,246,0.02)', 'rgba(59,130,246,0.04)', 'rgba(59,130,246,0.06)', 'rgba(59,130,246,0.08)'] },
                },
                axisLine: { lineStyle: { color: darkTheme.line } },
            },
            series: [{
                type: 'radar',
                data: [{
                    value: skillsData.map(s => s.proficiency),
                    lineStyle: { color: darkTheme.blue, width: 2 },
                    areaStyle: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            { offset: 0, color: 'rgba(59,130,246,0.4)' },
                            { offset: 1, color: 'rgba(6,182,212,0.1)' },
                        ]),
                    },
                    itemStyle: { color: darkTheme.cyan, borderColor: darkTheme.blue, borderWidth: 2 },
                    symbol: 'circle',
                    symbolSize: 6,
                }],
            }],
            tooltip: {
                trigger: 'item',
                backgroundColor: '#1a2332',
                borderColor: 'rgba(255,255,255,0.1)',
                textStyle: { color: '#e2e8f0', fontFamily: 'Pretendard, Inter, sans-serif' },
            },
        });
        window.addEventListener('resize', () => radarChart.resize());
    }

    // ─── Model Evolution Bar Chart ───
    const evolutionEl = document.getElementById('model-evolution-chart');
    if (evolutionEl && typeof projectsData !== 'undefined' && projectsData.length > 0) {
        const project = projectsData[0];
        if (project.model_evolution) {
            const evolutionChart = echarts.init(evolutionEl);
            const versions = project.model_evolution.map(m => m.version);
            const accuracies = project.model_evolution.map(m => m.accuracy);
            const models = project.model_evolution.map(m => m.model);

            const labels = project.model_evolution.map(m => m.version + (m.model !== 'Custom CNN' ? '\n(' + m.model + ')' : ''));

            const minAcc = Math.min(...accuracies);
            const maxAcc = Math.max(...accuracies);
            const yMin = Math.floor(minAcc - (maxAcc - minAcc) * 0.3);
            const yMax = Math.ceil(maxAcc + (maxAcc - minAcc) * 0.2);

            evolutionChart.setOption({
                tooltip: {
                    trigger: 'axis',
                    backgroundColor: '#1a2332',
                    borderColor: 'rgba(255,255,255,0.1)',
                    textStyle: { color: '#e2e8f0', fontFamily: 'Pretendard, Inter, sans-serif' },
                    formatter: (params) => {
                        const idx = params[0].dataIndex;
                        const mv = project.model_evolution[idx];
                        const badge = mv.production ? ' <span style="color:#10b981">★ 운영</span>' : '';
                        return `<strong>${mv.version}</strong>${badge}<br/>
                                Model: ${mv.model}<br/>
                                Classes: ${mv.classes}<br/>
                                Accuracy: <span style="color:#10b981;font-weight:bold">${mv.accuracy}%</span>`;
                    },
                },
                grid: { left: '8%', right: '8%', top: '15%', bottom: '20%' },
                xAxis: {
                    type: 'category',
                    data: labels,
                    axisLabel: { color: darkTheme.text, fontSize: 10, fontFamily: 'Pretendard, Inter, sans-serif', interval: 0 },
                    axisLine: { lineStyle: { color: darkTheme.line } },
                    axisTick: { show: false },
                },
                yAxis: {
                    type: 'value',
                    min: yMin,
                    max: yMax,
                    axisLabel: { color: darkTheme.text, fontSize: 10, formatter: '{value}%' },
                    splitLine: { lineStyle: { color: darkTheme.line } },
                },
                series: [{
                    type: 'bar',
                    data: accuracies.map((val, idx) => {
                        const isProduction = project.model_evolution[idx].production;
                        return {
                            value: val,
                            itemStyle: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                    { offset: 0, color: isProduction ? darkTheme.green : darkTheme.blue },
                                    { offset: 1, color: isProduction ? darkTheme.cyan : 'rgba(59,130,246,0.3)' },
                                ]),
                                borderRadius: [6, 6, 0, 0],
                            },
                        };
                    }),
                    barWidth: '35%',
                    label: {
                        show: true,
                        position: 'top',
                        color: '#e2e8f0',
                        fontSize: 13,
                        fontWeight: 'bold',
                        fontFamily: 'Pretendard, Inter, sans-serif',
                        formatter: '{c}%',
                    },
                }],
            });

            // Animate on scroll
            let animated = false;
            const obs = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !animated) {
                        animated = true;
                        evolutionChart.resize();
                    }
                });
            }, { threshold: 0.3 });
            obs.observe(evolutionEl);

            window.addEventListener('resize', () => evolutionChart.resize());
        }
    }
});
