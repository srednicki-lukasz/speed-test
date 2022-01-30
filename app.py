import speedtest

st = speedtest.Speedtest()

print('[1/2] Performing download speed test...')
print('Your download speed is', st.download(), '\n')

print('[2/2] Performing upload speed test...')
print('Your upload speed is', st.upload())
