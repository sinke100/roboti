(this.webpackJsonproboti=this.webpackJsonproboti||[]).push([[0],{12:function(e,t,n){},14:function(e,t,n){},16:function(e,t,n){"use strict";n.r(t);var a=n(1),r=n.n(a),i=n(3),s=n.n(i),c=(n(12),n(4)),o=n(5),h=n(7),b=n(6),d=Math.floor(1e4*Math.random())+1,l=n(0);console.log({Random:d});var j=function(e){var t=e.name;e.id;return Object(l.jsxs)("div",{className:"tc bg-light-blue dib br3 pa3 ma2 grow bw2 shadow-5",children:[Object(l.jsx)("img",{alt:"robots",src:"https://robohash.org/".concat(d+t.toLowerCase(),"?size=280x240")}),Object(l.jsx)("div",{children:Object(l.jsx)("h2",{className:"f3 font-family: avenir",children:t})})]})},u=function(e){var t=e.robots;return Object(l.jsx)("div",{children:t.map((function(e,n){return Object(l.jsx)(j,{id:t[n].id,name:t[n].name},n)}))})},m=[{id:1,name:"Sinke"},{id:2,name:"Tena"},{id:3,name:"Vec"},{id:4,name:"Anja"},{id:5,name:"Hamer"},{id:6,name:"Ivana"},{id:7,name:"Renato"},{id:8,name:"Doris"},{id:9,name:"Karlo"},{id:10,name:"Marija"}],f=function(e){var t=e.searchChange;return Object(l.jsx)("div",{className:"pa2",children:Object(l.jsx)("input",{className:"pa3 ba b--green bg-lightest-blue",type:"search",onChange:t})})},g=(n(14),function(e){Object(h.a)(n,e);var t=Object(b.a)(n);function n(){var e;return Object(c.a)(this,n),(e=t.call(this)).onSearchChange=function(t){e.setState({searchfield:t.target.value})},e.state={robots:m,searchfield:""},e}return Object(o.a)(n,[{key:"render",value:function(){var e=this,t=this.state.robots.filter((function(t){return t.name.toLowerCase().includes(e.state.searchfield.toLowerCase())}));return console.log(t),this.state.robots.length?Object(l.jsxs)("div",{className:"tc",children:[Object(l.jsx)("h1",{className:"f1",children:"Roboti"}),Object(l.jsx)("p",{children:d}),Object(l.jsx)(f,{searchChange:this.onSearchChange}),Object(l.jsx)(u,{robots:t})]}):Object(l.jsx)("h1",{children:"Loading"})}}]),n}(r.a.Component)),O=(n(15),function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,17)).then((function(t){var n=t.getCLS,a=t.getFID,r=t.getFCP,i=t.getLCP,s=t.getTTFB;n(e),a(e),r(e),i(e),s(e)}))});s.a.render(Object(l.jsx)(g,{}),document.getElementById("root")),O()}},[[16,1,2]]]);
//# sourceMappingURL=main.0dbbbb86.chunk.js.map