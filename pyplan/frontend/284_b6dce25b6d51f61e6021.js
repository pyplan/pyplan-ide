/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[284],{739:function(t,e,n){"use strict";(function(c){var s,i=n(679);void 0===(s=function(){return c.Model.extend({url:"myFileManager",getTask:function(t,e){(0,i.send)("scheduler/".concat(t,"/"),null,{type:"GET"},e)},getTaskLog:function(t,e){(0,i.send)("taskLog/by_periodic_task/",t,{type:"POST"},e,null,!0)},filterLogs:function(t,e,n){(0,i.send)("taskLog/filter_logs/?page=".concat(t),JSON.stringify(e),{type:"POST",contentType:"application/json;charset=utf-8"},n,null,!0)},create:function(t,e,n){(0,i.send)("scheduler/",JSON.stringify(t),{type:"POST",contentType:"application/json;charset=utf-8",dataType:"text"},e,n,!1,!0)},edit:function(t,e,n){(0,i.send)("scheduler/".concat(t.id,"/"),JSON.stringify(t),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},e,n,!1,!0)},partialEdit:function(t,e,n,c){(0,i.send)("scheduler/".concat(t,"/"),JSON.stringify(e),{type:"PATCH",contentType:"application/json;charset=utf-8",dataType:"text"},n,c,!1,!0)},list:function(t,e){(0,i.send)("scheduler/",null,{type:"GET"},t,e)},deleteTask:function(t,e){(0,i.send)("scheduler/".concat(t,"/"),null,{type:"DELETE"},e)},runTask:function(t,e){var n=t.periodic_task_id;t.scheduleTaskId;(0,i.send)("scheduler/".concat(n,"/runTask/"),null,{type:"POST"},e)},getPythonTimezones:function(t,e){(0,i.send)("scheduler/getPythonTimezones/",null,{type:"GET"},t,e)}})}.apply(e,[]))||(t.exports=s)}).call(this,n(219))}}]);