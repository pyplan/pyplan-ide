/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[121],{1148:function(n,e,t){"use strict";(function(i,a){var l,r;l=[t(1449),t(1450)],void 0===(r=function(n,e){return i.View.extend({el:a("#main"),inQuery:!1,render:function(){var n=e();this.$el.append(n),this.addHandlers()},addHandlers:function(){var e=this,t=e.$el.find(".dbAdmin"),i=t.find(".sqlEditor").get()[0];ace.require("ace/ext/language_tools");var l=ace.edit(i);l.setTheme("ace/theme/sqlserver"),l.getSession().setMode("ace/mode/sqlserver"),l.setHighlightActiveLine(!1),l.setShowPrintMargin(!1),l.setOptions({enableBasicAutocompletion:!0,enableSnippets:!1,enableLiveAutocompletion:!0}),t.find("input[name='connectString']").val(a.cookie("cubeplanmilano_lastcn"));var r=a.cookie("cubeplanmilano_lastquery");r&&l.setValue(r),this.$el.find(".dbAdmin .btnRun").on("click",function(){if(!e.inQuery){e.inQuery=!0,e.$el.find(".dbAdmin .query-result").html("Running...");var i={connectString:t.find("input[name='connectString']").val(),query:l.getValue()};(new n).runQuery(i,function(n){e.inQuery=!1,e.renderResult(n)},function(){e.inQuery=!1}),a.cookie("cubeplanmilano_lastcn",i.connectString),a.cookie("cubeplanmilano_lastquery",i.query)}})},renderResult:function(n){this.$el.find(".dbAdmin .query-result").html(n)}})}.apply(e,l))||(n.exports=r)}).call(this,t(218),t(1))},1449:function(n,e,t){"use strict";(function(i){var a,l=t(693);void 0===(a=function(){return i.Model.extend({runQuery:function(n,e,t){(0,l.send)("DBAdmin/runQuery",n,{type:"POST"},e,t)}})}.apply(e,[]))||(n.exports=a)}).call(this,t(218))},1450:function(n,e,t){var i=t(690);function a(n){return n&&(n.__esModule?n.default:n)}n.exports=(i.default||i).template({compiler:[7,">= 4.0.0"],main:function(n,e,i,l,r){var s=null!=e?e:n.nullContext||{},o=n.escapeExpression;return'<div class="abm-base-tmp container-fluid mainTask dbAdmin" data-rel="dbadmin" data-type="tab-content" >\n    <div class="row-fluid">\n        <div class="span12">\n            <div class="box box-bordered box-color">\n                <div class="box-title">\n                    <h3><i class="fa fa-th-list"></i>'+o(a(t(688)).call(s,"DBAdmin",{name:"L",hash:{},data:r}))+'</h3>\n                </div>\n                <div class="box-content">\n\n\n                    <label>'+o(a(t(688)).call(s,"connection_string",{name:"L",hash:{},data:r}))+'</label>\n                    <input type="text" class="form-control" name="connectString" />\n                    <br/>\n                    <label>'+o(a(t(688)).call(s,"query",{name:"L",hash:{},data:r}))+'</label>\n                    <div class="sqlEditor"></div>\n                    <br/>\n\n                    <button class="btnRun btn btn-grey-1">'+o(a(t(688)).call(s,"run_query",{name:"L",hash:{},data:r}))+'</button>\n\n                    <div class="query-result">\n\n                    </div>\n\n                </div>\n            </div>\n        </div>\n    </div>\n</div>'},useData:!0})},688:function(n,e,t){"use strict";var i=t(18);n.exports=function(n){return(0,i.translate)(n)}}}]);