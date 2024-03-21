# DWave token generation (Semi-auto)
> This script semi-automatically generates a D-Wave token (typically within 1 min)

> The process involves two phases: 1. sign up by input email; 2. sign in by activation link & get dwave token

## How to use
### Set up
1. Install necessary packages:  
`pip install -r requirements.txt`
2. Have a web browser (Chrome, Edge,...)
3. If you are in a country not supported by D-Wave (e.g., Vietnam), use a VPN to change your IP address to the US.

### Get token

1. Get a temp email at [temp-mail.org](https://temp-mail.org/)
2. Run  
```python main.py <temp email>```
- The input email will be signed up and Dwave'll send an activation link to this email  
3. Take activation link also at [temp-mail.org](https://temp-mail.org/)
4. Paste activation link after receiving this request from program:
`Enter activation link:`
5. The token will be printed in screen and saved in `output/all_token.txt`

#### Example
```
> python main.py "hewow42726@hdrlog.com"
Enter activation link:
> https://cloud.dwavesys.com/leap/activate/MTY2Nzcw/c476zq-351a10e872a37244d1cc/
```