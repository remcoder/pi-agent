# Pi Agent - reporting the health of your Raspberry Pi via GPT

```mermaid
flowchart TD 
A[Start] --> B[Collect System Metrics]
B --> D[Analyze Report with GPT-3]
D --> F{Is Alert Needed?}
F -->|True|G[Send Notification]
F -->|False|H[Log Status & Exit] 
G --> I[End] 
H --> I
```

<img src="https://github.com/remcoder/pi-agent/assets/461650/604f182c-b838-4b75-bb16-8824d6e74fd0" width=300 />
