## tutorial envoy example
https://www.youtube.com/watch?v=JrbmNAP-s9s

using the envoy filter the faults are controlled by headers:

https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/fault_filter

using hey as our load test tool and setting the http status and percentage, etc

## status code example
```
xcxl200@C02F73NKMD6R ~/g/d/envoy_fault_injection_examples ❯❯❯ hey -c 1 -n 100  -H "x-envoy-fault-abort-request: 503" -H "x-envoy-fault-abort-request-percentage: 50" http://localhost:9090

Summary:
  Total:        0.5306 secs
  Slowest:      0.0133 secs
  Fastest:      0.0002 secs
  Average:      0.0053 secs
  Requests/sec: 188.4782

  Total data:   1890 bytes
  Size/request: 18 bytes

Response time histogram:
  0.000 [1]     |■
  0.001 [53]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.003 [0]     |
  0.004 [0]     |
  0.005 [0]     |
  0.007 [0]     |
  0.008 [0]     |
  0.009 [0]     |
  0.011 [2]     |■■
  0.012 [40]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.013 [4]     |■■■


Latency distribution:
  10% in 0.0002 secs
  25% in 0.0003 secs
  50% in 0.0004 secs
  75% in 0.0110 secs
  90% in 0.0114 secs
  95% in 0.0118 secs
  99% in 0.0133 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0001 secs, 0.0002 secs, 0.0133 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0013 secs
  req write:    0.0000 secs, 0.0000 secs, 0.0001 secs
  resp wait:    0.0051 secs, 0.0001 secs, 0.0132 secs
  resp read:    0.0000 secs, 0.0000 secs, 0.0001 secs

Status code distribution:
  [200] 45 responses
  [503] 55 responses

```

# time delay example
```
[I] xcxl200@C02F73NKMD6R ~>  time curl -H "x-envoy-fault-delay-request: 3000" -H "x-envoy-fault-delay-request-percentage: 50" http://localhost:9090

{"message":"Hello"}

________________________________________________________
Executed in    3.03 secs      fish           external
   usr time    4.10 millis  129.00 micros    3.98 millis
   sys time    6.88 millis  716.00 micros    6.17 millis
```

# response rate limit example

```
xcxl200@C02F73NKMD6R ~/g/d/envoy_fault_injection_examples ❯❯❯ curl -H "x-envoy-fault-throughput-response: 1000" --output dest.dat localhost:9090/static/50mbfile.dat
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
 29 50.0M   29 14.6M    0     0   939k      0  0:00:54  0:00:16  0:00:38  787k


```