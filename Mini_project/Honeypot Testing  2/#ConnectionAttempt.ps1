# Connect to the honeypot
$socket = New-Object System.Net.Sockets.TcpClient("localhost", 12345)

# Send data to the honeypot
$stream = $socket.GetStream()
$stream.Write([System.Text.Encoding]::UTF8.GetBytes("Hello from PowerShell"), 0, 15)

# Close the connection
$socket.Close()