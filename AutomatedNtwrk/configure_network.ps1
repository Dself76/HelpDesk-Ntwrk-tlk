# Requires running as Administrator
Param(
    [string]$IPAddress = "192.168.1.100",
    [string]$SubnetMask = "255.255.255.0",
    [string]$Gateway = "192.168.1.1",
    [string]$DNS1 = "8.8.8.8",
    [string]$DNS2 = "8.8.4.4"
)

Write-Host "Configuring Network Settings..."

# Set IP Address, Subnet Mask, and Gateway
New-NetIPAddress -IPAddress $IPAddress -PrefixLength 24 -DefaultGateway $Gateway

# Set DNS Server Addresses
Set-DnsClientServerAddress -ServerAddresses ($DNS1, $DNS2)

Write-Host "Network configuration completed successfully."
