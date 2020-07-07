/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[167],{2640:function(n,a,t){"use strict";(function(e,l){var s,o,i=t(18);s=[t(2641),t(2642),t(2643)],void 0===(o=function(n,a,s){return e.View.extend({el:l("#main"),render:function(n){var t=this,e=a();this.$el.append(e),l("#dataSnapshot").on("hidden.bs.modal",(function(){l("#dataSnapshot  .searchNode").select2("destroy"),l("#dataSnapshot").off("hidden"),l("#dataSnapshot").remove()})).modal("show"),setTimeout((function(){t.addHandlers(l("#dataSnapshot")),t.loadList(l("#dataSnapshot"))}),200)},addHandlers:function(a){t.e(69).then((function(){var n=[t(1590)];(function(n){(new n).create({el:"#dataSnapshot .searchNode",filteredClasses:["variable","constant"]})}).apply(null,n)})).catch(t.oe),a.find(".searchNode").on("change",(function(){var n=l(this).select2("data");if(0==a.find(".inputData ul li[data-id='"+n.id+"']").length){var t=s(n);a.find(".inputData ul").append(t)}a.find(".searchNode").select2("val","")})),l("#dataSnapshot").on("updateProgress",(function(n,t){t&&(a.find(".progressBar div.progress-bar").css("width",t.percent+"%"),a.find(".progressBar p").html((0,i.translate)("saving")+" "+t.nodeTitle+" ..."))})),a.find(".node-list ul").on("click","li .remover",(function(){l(this).closest("li").remove()})),a.find(".btnCreate").on("click",(function(){var t=[];if(a.find(".node-list li").each((function(n,a){t.push({nodeId:l(this).attr("data-id")})})),t.length>0){var e={name:"Data snapshot scenario",description:"Data snapshot scenario",nodeList:t};a.find(".inputData").hide(),a.find(".progressBar").show(),a.find(".progressBar div.bar").css("width","10%"),a.find(".progressBar p").html((0,i.translate)("saving")+" ..."),(new n).updateDataSnapshot(e,(function(){a.find(".progressBar div.bar").css("width","100%"),setTimeout((function(){a.find(".progressBar").hide(),a.find(".createResult").show(),a.find(".createResult button").show()}),300)}),(function(){a.find(".createResult").hide(),a.find(".inputData").show()}))}return!1})),a.find(".controls .btnDelete").on("click",(function(){l(this).hasClass("disabled")||(a.find(".controls button").hide(),a.find(".controls .btnSure").show())})),a.find(".controls .btnCancel").on("click",(function(){a.find(".controls button").show(),a.find(".controls .btnSure").hide()})),a.find(".controls .btnGoDelete").on("click",(function(){a.find(".controls btnSure").hide(),(new n).clearDataSnapshot((function(){a.modal("hide")}))})),a.find(".controls .btnClose").on("click",(function(){a.modal("hide")}))},loadList:function(a){(new n).getCurrentNodesInSnapshot((function(n){n&&n.length>0&&(a.find(".controls .btnDelete").removeClass("disabled"),l.each(n,(function(n,t){var e=s(t);a.find(".inputData ul").append(e)})))}))}})}.apply(a,s))||(n.exports=o)}).call(this,t(219),t(1))},2641:function(n,a,t){"use strict";(function(e){var l,s=t(679);void 0===(l=function(){return e.Model.extend({getCurrentNodesInSnapshot:function(n,a){(0,s.send)("DataSnapshot/getCurrentNodesInSnapshot",null,null,n,a)},updateDataSnapshot:function(n,a,t){(0,s.send)("DataSnapshot/updateDataSnapshot",n,{type:"POST"},a,t)},clearDataSnapshot:function(n,a){(0,s.send)("DataSnapshot/clearDataSnapshot",null,null,n,a)}})}.apply(a,[]))||(n.exports=l)}).call(this,t(219))},2642:function(n,a,t){var e=t(670);function l(n){return n&&(n.__esModule?n.default:n)}n.exports=(e.default||e).template({compiler:[8,">= 4.3.0"],main:function(n,a,e,s,o){var i=null!=a?a:n.nullContext||{},d=n.escapeExpression;return'<div id="dataSnapshot" class="modal fade" tabindex="-1" role="dialog" style="display: none;">\n    <div class="modal-dialog">\n        <div class="modal-content">\n            <div class="modal-header">\n                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button>\n                <h3>'+d(l(t(668)).call(i,"data_snapshot",{name:"L",hash:{},data:o,loc:{start:{line:6,column:20},end:{line:6,column:41}}}))+'</h3>\n            </div>\n\n            <div class="modal-body">\n\n                <div class="inputData">\n                    <h5>'+d(l(t(668)).call(i,"data_snapshot_explain",{name:"L",hash:{},data:o,loc:{start:{line:12,column:24},end:{line:12,column:53}}}))+'</h5>\n\n                    <div class="node-list nodeslist">\n                        <ul>\n\n                        </ul>\n                    </div>\n\n                    <div>\n                        <h5>'+d(l(t(668)).call(i,"add_node_to_snapshot",{name:"L",hash:{},data:o,loc:{start:{line:21,column:28},end:{line:21,column:56}}}))+'</h5>\n                        <input class="searchNode">\n                        \x3c!--<button class="btn btnAddNode btn-small">'+d(l(t(668)).call(i,"add_node",{name:"L",hash:{},data:o,loc:{start:{line:23,column:69},end:{line:23,column:85}}}))+'</button>--\x3e\n                    </div>\n\n                    <div class="controls">\n                        <button class="btn btnDelete btn-small btn-red disabled"><i class="fa fa-trash"></i>\n                            '+d(l(t(668)).call(i,"delete_data_snapshot",{name:"L",hash:{},data:o,loc:{start:{line:28,column:28},end:{line:28,column:56}}}))+'</button>\n                        <button class="btn btnCreate btn-primary btn-small"><i class="fa fa-file"></i>\n                            '+d(l(t(668)).call(i,"create_data_snapshot",{name:"L",hash:{},data:o,loc:{start:{line:30,column:28},end:{line:30,column:56}}}))+'</button>\n\n                        <button class="btn btn-small btn-grey nodisplay btnCancel btnSure"></i> '+d(l(t(668)).call(i,"cancel",{name:"L",hash:{},data:o,loc:{start:{line:32,column:96},end:{line:32,column:110}}}))+'</button>\n                        <button class="btn btn-small btn-red nodisplay btnGoDelete btnSure">'+d(l(t(668)).call(i,"yes",{name:"L",hash:{},data:o,loc:{start:{line:33,column:92},end:{line:33,column:103}}}))+'</button>\n                        <span class="btnSure nodisplay">'+d(l(t(668)).call(i,"sure_clear_snapshot",{name:"L",hash:{},data:o,loc:{start:{line:34,column:56},end:{line:34,column:83}}}))+'</span>\n\n                    </div>\n\n                </div>\n\n                <div class="progressBar nodisplay">\n                    <p>'+d(l(t(668)).call(i,"saving",{name:"L",hash:{},data:o,loc:{start:{line:41,column:23},end:{line:41,column:37}}}))+' ...</p>\n                    <div class="progress progress-striped active">\n                        <div class="progress-bar" style="width: 10%;"></div>\n                    </div>\n                </div>\n\n                <div class="createResult nodisplay">\n                    <p>'+d(l(t(668)).call(i,"data_snapshot_created",{name:"L",hash:{},data:o,loc:{start:{line:48,column:23},end:{line:48,column:52}}}))+'</p>\n\n                    <div class="controls">\n                        <button class="btn btnClose btn-small">'+d(l(t(668)).call(i,"close",{name:"L",hash:{},data:o,loc:{start:{line:51,column:63},end:{line:51,column:76}}}))+"</button>\n                    </div>\n                </div>\n\n            </div>\n\n        </div>\n    </div>\n</div>"},useData:!0})},2643:function(n,a,t){var e=t(670);n.exports=(e.default||e).template({compiler:[8,">= 4.3.0"],main:function(n,a,t,e,l){var s,o=null!=a?a:n.nullContext||{},i=n.hooks.helperMissing,d=n.escapeExpression,c=n.lookupProperty||function(n,a){if(Object.prototype.hasOwnProperty.call(n,a))return n[a]};return'<li data-id="'+d("function"==typeof(s=null!=(s=c(t,"id")||(null!=a?c(a,"id"):a))?s:i)?s.call(o,{name:"id",hash:{},data:l,loc:{start:{line:1,column:13},end:{line:1,column:19}}}):s)+'">\n    <span class="node">\n        <i class="fa fa-remove remover"></i>\n        <i class="icon-'+d("function"==typeof(s=null!=(s=c(t,"nodeClass")||(null!=a?c(a,"nodeClass"):a))?s:i)?s.call(o,{name:"nodeClass",hash:{},data:l,loc:{start:{line:4,column:23},end:{line:4,column:36}}}):s)+'"></i>   \n        <span class="nodeTitle">'+d("function"==typeof(s=null!=(s=c(t,"name")||(null!=a?c(a,"name"):a))?s:i)?s.call(o,{name:"name",hash:{},data:l,loc:{start:{line:5,column:32},end:{line:5,column:40}}}):s)+'</span>\n        <span class="nodeId">'+d("function"==typeof(s=null!=(s=c(t,"id")||(null!=a?c(a,"id"):a))?s:i)?s.call(o,{name:"id",hash:{},data:l,loc:{start:{line:6,column:29},end:{line:6,column:35}}}):s)+"</span>\n    </span>\n</li>"},useData:!0})}}]);