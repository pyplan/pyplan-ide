/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[27],{747:function(n,e,t){"use strict";(function(o){var c;void 0===(c=function(){return o.Controller.extend({name:"knowledgeBase",showTaskScheduler:function(){t.e(265).then(function(){var n=[t(2048)];(function(n){(new n).render()}).apply(null,n)}).catch(t.oe)},showRunModelTask:function(n){t.e(79).then(function(){var e=[t(1331)];(function(e){(new e).render(n)}).apply(null,e)}).catch(t.oe)},showOledbTask:function(n){t.e(80).then(function(){var e=[t(1332)];(function(e){(new e).render(n)}).apply(null,e)}).catch(t.oe)},showEtlTask:function(n,e){t.e(81).then(function(){var o=[t(1333)];(function(t){new t({tasksList:e}).render(n)}).apply(null,o)}).catch(t.oe)},listTasks:function(n){t.e(266).then(function(){var e=[t(2054)];(function(e){new e({taskType:n}).render()}).apply(null,e)}).catch(t.oe)},showTaskLogs:function(n){t.e(267).then(function(){var e=[t(2056)];(function(e){new e({taskQuery:n,title:"Task log"}).render()}).apply(null,e)}).catch(t.oe)},addScheduleTask:function(n,e,o){n=n;switch(e){case"model-tasks":t.e(79).then(function(){var e=[t(1331)];(function(e){(new e).render(n)}).apply(null,e)}).catch(t.oe);break;case"oledb-tasks":t.e(80).then(function(){var e=[t(1332)];(function(e){(new e).render(n)}).apply(null,e)}).catch(t.oe);break;case"etl-tasks":t.e(81).then(function(){var e=[t(1333)];(function(e){new e({tasksList:o}).render(n)}).apply(null,e)}).catch(t.oe)}},showOpenModelSelector:function(n){t.e(268).then(function(){var e=[t(2059)];(function(e){(new e).render(n)}).apply(null,e)}).catch(t.oe)}})}.apply(e,[]))||(n.exports=c)}).call(this,t(694))}}]);