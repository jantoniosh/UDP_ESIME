const dgram = require('dgram');

let PORT = 33333;
let HOST = '192.168.1.40';

let client = dgram.createSocket('udp4');
let conta = 0;

setInterval(() => {
    let message = new Buffer.from(conta.toString());
    client.send(message, 0, message.length, PORT, HOST, function (err, bytes) {
        if (err) throw err;
    });
    console.log(conta);
    conta = conta + 1;
}, 1000);
