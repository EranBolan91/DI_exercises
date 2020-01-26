let allBooks = [{
    title: "Secrets of the javascript Ninja",
    author:"Br bibo and Jeson resing",
    image:'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrZrfDTo8K6_RHOU6GSdPkbBZQRnCmYp-iRlhCkZs7BHsl5ozo',
    alreadyRead:false
},{
    title: "HTML5 for Web Designers",
    author:"Jermi Kith",
    image:'https://html5forwebdesigners.com/img/cover.png',
    alreadyRead:true  
}]

for (let i = 0; i < allBooks.length; i++) {
    let h1 = document.createElement('h1');
    h1.innerHTML = allBooks[i].title;
    document.body.appendChild(h1);

    let h3 = document.createElement('h3');
    h3.innerHTML = allBooks[i].title + " written by " + allBooks[i].author;
    document.body.appendChild(h3);

    let image = document.createElement('img');
      image.setAttribute("src", allBooks[i].image);
      image.setAttribute("width", "100");
      image.setAttribute("height", "228");
      image.setAttribute("alt", allBooks[i].title);
      document.body.appendChild(image);

    if(allBooks[i].alreadyRead == true){
        h1.style.backgroundColor = "red";
        h3.style.backgroundColor = "red";
        image.style.backgroundColor = "red";
    }
    
}


