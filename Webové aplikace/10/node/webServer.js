const http = require('http');

// request a response jsou stream
const server = http.createServer((request, response) => {
  const { headers, method, url } = request;
    
  let body = [];
  
  request.on('error', (err) => {
    console.error(err);
  });
    
  request.on('data', (chunk) => {
    body.push(chunk);
  });
    
  request.on('end', () => {
    body = Buffer.concat(body).toString();
  
    response.on('error', (err) => {
      console.error(err);
    });
  
    const responseBody = { headers, method, url, body };
      
    // HTTP status, hlavicka
    response.writeHead(200, {'Content-Type': 'application/json'})
    response.write(JSON.stringify(responseBody));
    response.end();
  });
});
  
server.listen(8080);