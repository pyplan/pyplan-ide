/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[35],{748:function(n,e,t){"use strict";(function(o){var c;void 0===(c=function(){return o.Controller.extend({name:"knowledgeBase",showTaskScheduler:function(){t.e(171).then((function(){var n=[t(2616)];(function(n){(new n).render()}).apply(null,n)})).catch(t.oe)},showRunModelTask:function(n){t.e(67).then((function(){var e=[t(1640)];(function(e){(new e).render(n)}).apply(null,e)})).catch(t.oe)},showOledbTask:function(n){t.e(76).then((function(){var e=[t(1641)];(function(e){(new e).render(n)}).apply(null,e)})).catch(t.oe)},showEtlTask:function(n,e){t.e(65).then((function(){var o=[t(1642)];(function(t){new t({tasksList:e}).render(n)}).apply(null,o)})).catch(t.oe)},listTasks:function(n){t.e(201).then((function(){var e=[t(2622)];(function(e){new e({taskType:n}).render()}).apply(null,e)})).catch(t.oe)},showTaskLogs:function(n){t.e(172).then((function(){var e=[t(2624)];(function(e){new e({taskQuery:n,title:"Task log"}).render()}).apply(null,e)})).catch(t.oe)},addScheduleTask:function(n,e,o){n=n;switch(e){case"model-tasks":t.e(67).then((function(){var e=[t(1640)];(function(e){(new e).render(n)}).apply(null,e)})).catch(t.oe);break;case"oledb-tasks":t.e(76).then((function(){var e=[t(1641)];(function(e){(new e).render(n)}).apply(null,e)})).catch(t.oe);break;case"etl-tasks":t.e(65).then((function(){var e=[t(1642)];(function(e){new e({tasksList:o}).render(n)}).apply(null,e)})).catch(t.oe)}},showOpenModelSelector:function(n){t.e(161).then((function(){var e=[t(2627)];(function(e){(new e).render(n)}).apply(null,e)})).catch(t.oe)}})}.apply(e,[]))||(n.exports=c)}).call(this,t(677))}}]);