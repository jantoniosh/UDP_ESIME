const dgram = require('dgram');

let PORT = 33333;
let HOST = '0.0.0.0';

let server = dgram.createSocket('udp4');

server.on('listening', function () {
    let address = server.address();
    console.log('UDP Server listening on ' + address.address + ':' + address.port);
});

server.on('message', function (message, remote) {
    console.log(remote.address + ':' + remote.port + ' - ' + message);
});

server.bind(PORT, HOST);