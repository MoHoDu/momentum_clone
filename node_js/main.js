var http = require('http');
var fs = require('fs');
var url = require('url');
// 우리는 url이라고 하는 모듈을 사용할 것이다
// 앞으로 url이라는 노드는 url이라는 변수를 통해서 사용할 것이다

var app = http.createServer(function(request,response){
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var title = queryData.id;
    console.log(queryData.id);
    if(_url == '/'){
      title = 'Welcome';
    }
    if(_url == '/favicon.ico'){
      return response.writeHead(404);
    }
    response.writeHead(200);
    fs.readFile(`data/${queryData.id}`, 'utf-8', function(err, description) {
      var template = `
      <!doctype html>
      <html>
      <head>
      <title>WEB1 - ${title}</title>
      <meta charset="utf-8">
      </head>
      <body>
      <h1><a href="/">WEB</a></h1>
      <ol>
          <li><a href="/?id=HTML">HTML</a></li>
          <li><a href="/?id=CSS">CSS</a></li>
          <li><a href="/?id=JavaScript">JavaScript</a></li>
      </ol>
      <h2>${title}</h2>
      <p>${description}</p>
      </body>
      </html>
      `;
      response.end(template);
      // template만 바꾸면 1억개의 페이지를 한번에 바뀜
    })
});
app.listen(3000);