/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[152,7],{2388:function(e,n,t){"use strict";(function(o,l){var a,s,i=t(18);a=[t(663),t(2389),t(767)],void 0===(s=function(e,n,t){return o.View.extend({el:l("#main"),render:function(o,a,s){var c=n({url:o});(new e).show({title:"Delete",html:c,modalClass:"shortModal",buttons:[{title:(0,i.translate)("cancel"),code:"close"},{title:(0,i.translate)("delete"),css:"red",code:"yes"}],callback:function(e,n){if("yes"==e)return n.modal("hide"),(new t).deleteAttachedFile(o,(function(e){s(a,e)})),!1},onLoad:function(e){setTimeout((function(){l("#main-modal button.btn-primary").focus()}),500)}})}})}.apply(n,a))||(e.exports=s)}).call(this,t(219),t(1))},2389:function(e,n,t){var o=t(670);e.exports=(o.default||o).template({compiler:[8,">= 4.3.0"],main:function(e,n,t,o,l){return'<div class="box">\n\n       <span>Are you sure you want to delete this attached file?</span>\n\n   <div class="box-content">\n\n\n\n</div>\n'},useData:!0})},663:function(e,n,t){"use strict";(function(o){var l;void 0===(l=function(){return o.Controller.extend({name:"showModal",show:function(e){Promise.all([t.e(2),t.e(228)]).then((function(){var n=[t(686)];(function(n){(new n).render(e)}).apply(null,n)})).catch(t.oe)}})}.apply(n,[]))||(e.exports=l)}).call(this,t(677))},767:function(e,n,t){"use strict";(function(o){var l,a=t(679);void 0===(l=function(){return o.Model.extend({url:"knowledgeBase",getPost:function(e,n){(0,a.send)("KnowledgeBase/getPost?nodeId="+e,null,{type:"GET"},n)},search:function(e,n){(0,a.send)("KnowledgeBase/search",e,{type:"POST"},n)},generatePost:function(e,n){(0,a.send)("KnowledgeBase/generatePost?nodeId="+e,null,{type:"POST"},n)},updatePost:function(e,n){(0,a.send)("KnowledgeBase/updatePost",e,{type:"PUT"},n)},deleteAttachedFile:function(e,n){(0,a.send)("KnowledgeBase/deleteDocument?url="+e,null,{type:"DELETE"},n)}})}.apply(n,[]))||(e.exports=l)}).call(this,t(219))}}]);