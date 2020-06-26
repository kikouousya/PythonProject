var tag=document.createElement("input");
    tag.setAttribute('type','text');
tag.appendChild(newnode);
tag.insertBefore(newnode,某个节点);

var ele = document.createElement("img");
ele.setAttribute("src","1.jpg");
ele.src = "1.jpg";
var con = document.getElementById("div1")[0];
var delTarget = con.getElementsByTagName("h1")[0];
con.removeChild(delTarget);