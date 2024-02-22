# Pi Agent - reporting the health of your Raspberry Pi via GPT

- collect system information via:
   - mpstat -o JSON
   - df -h
   - free -h
   - pgrep -f octoprint
   - vcgencmd measure_temp
 - ask GPT what to make of this and whether to raise an alarm
 - send notification via Pushover



<img src="https://github.com/remcoder/pi-agent/assets/461650/94084cb5-d2be-4b66-9c6f-6af87dc8c042" width=300 />

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
