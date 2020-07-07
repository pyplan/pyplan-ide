/*! Copyright Pyplan 2020. All rights reserved. */
(window.webpackJsonp=window.webpackJsonp||[]).push([[173],{2705:function(e,n,t){"use strict";(function(l,a){var i,o,s=t(18);t(2706),t(2707),i=[t(2710)],void 0===(o=function(e){var n=l.View.extend({el:a("#main"),render:function(t){if(!(this.$el.find("#main-modal").length>0)){var l=this,i=e(t);this.$el.append(i);var o=this.$el;this.loadSelectLists(o);var c="";a.each(t.itemProperties.menuDefinition,(function(e,n){c+=function e(n){var t="<li class='dd-item' data-id='"+n.id+"'data-title='"+n.title+"'data-subtitle='"+n.subtitle+"'data-icon='"+n.icon+"'data-action='"+n.action+"'data-blank-target='"+n.blankTarget+"'data-tasklog-id='"+n.tasklogId+"'data-hidden-dpts='"+n.hiddenDpts+"'data-dash-id='"+n.dashId+"'data-url='"+n.url+"'><div class='dd-handle'>"+n.title+"  </div> <i class='fa fa-pencil btnEditItem' /><i class='fa fa-close btnRemoveItem' />";return n.children&&(t+="<ol class='dd-list'>",a.each(n.children,(function(n,l){t+=e(l)})),t+="</ol>"),t+="</li>"}(n)})),this.$el.find(".dd-list").html(c),this.$el.find(".dd").nestable(),(0,s.postRender)(o),o.find(".selItemsAlign").val(t.itemProperties.generalSettings.itemsAlign),o.find(".selTextAlign").val(t.itemProperties.generalSettings.textAlign),o.find(".spectrum-colors").colorPicker("",{allowEmpty:!0,chooseText:"Ok",cancelText:"",change:function(e){var l=a(this).attr("data-key"),i="transparent";if(e&&(i=e.toHexString()),n){switch(l){case"menu-title-color":t.itemProperties.generalSettings.menuTitleColor=i;break;case"bg-color":t.itemProperties.generalSettings.backgroundColor=i;break;case"hover-color":t.itemProperties.generalSettings.hoverBackgroundColor=i;break;case"text-color":t.itemProperties.generalSettings.textColor=i;break;case"icon-color":t.itemProperties.generalSettings.iconColor=i}o.find(".inline-color[data-format-key='".concat(l,"']")).css("background-color",i),o.find(".color-selector[data-format-key='".concat(l,"']")).css("background-color",i)}}}),a("button.btnAddItem").on("click",(function(){var e="<li class='dd-item' data-id='"+(o.find(".dd-handle").length+1)+"'data-title='New Item'data-subtitle=''data-icon='fa fa-plus'data-action='noAction'data-blank-target='false'data-tasklog-id='0'data-dash-id='0'><div class='dd-handle'>New Item </div> <i class='fa fa-pencil btnEditItem' /><i class='fa fa-close btnRemoveItem' /> </li>";l.$el.find(".dd > ol.dd-list").append(e),l.$el.find(".dd .dd-empty").remove(),l.$el.find(".dd").nestable()})),o.on("click","i.btnRemoveItem",(function(){var e=a(this).closest("li").attr("data-id");l.$el.find(".dd").nestable("remove",e)})),o.on("click",'a[data-toggle="tab"].disabled',(function(e){return e.preventDefault(),!1})),o.on("click","i.btnEditItem",(function(){o.find(".drawMenuTab2").removeClass("disabled"),o.find(".drawMenuTab3").removeClass("disabled"),o.find(".drawMenuTab2").click(),l.$el.find(".dd-handle").removeClass("selected"),a(this).parent().find(">.dd-handle").addClass("selected");var e=a(this).closest("li.dd-item");l.populateForm(e,o)})),o.on("keyup",'.itemSettings input[type="text"]',(function(){var e=o.find(".dd-handle.selected").closest("li");switch(a(this).attr("data")){case"title":e.attr("data-title",o.find(".txtTitle").val()),e.data("title",o.find(".txtTitle").val()),o.find(".dd-handle.selected").html(o.find(".txtTitle").val());break;case"subtitle":e.attr("data-subtitle",o.find(".txtSubtitle").val()),e.data("subtitle",o.find(".txtSubtitle").val());break;case"icon":e.attr("data-icon",o.find(".txtIcon").val()),e.data("icon",o.find(".txtIcon").val())}})),o.on("keyup",".txtMenuTitle",(function(){var e=a(this).val();t.itemProperties.generalSettings.menuTitle=e})),o.on("keyup",".txtMenuTitleSize",(function(){var e=a(this).val();t.itemProperties.generalSettings.menuTitleSize=e})),o.on("change",".selItemsAlign",(function(){var e=a(this).val();t.itemProperties.generalSettings.itemsAlign=e})),o.on("change",".selTextAlign",(function(){var e=a(this).val();t.itemProperties.generalSettings.textAlign=e})),o.on("keyup",".txtItemsPerRow",(function(){var e=a(this).val();t.itemProperties.generalSettings.itemsPerRow=e})),o.on("keyup",".txtTitleMargin",(function(){var e=a(this).val();t.itemProperties.generalSettings.titleMargin=e})),o.on("keyup",".txtSubtitleMargin",(function(){var e=a(this).val();t.itemProperties.generalSettings.subtitleMargin=e})),o.on("keyup",".txtTitleSize",(function(){var e=a(this).val();t.itemProperties.generalSettings.titleSize=e})),o.on("keyup",".txtSubtitleSize",(function(){var e=a(this).val();t.itemProperties.generalSettings.subtitleSize=e})),o.on("keyup",".txtIconSize",(function(){var e=a(this).val();t.itemProperties.generalSettings.iconSize=e})),o.on("keyup",".txtIconMarginTop",(function(){var e=a(this).val();t.itemProperties.generalSettings.iconMarginTop=e})),o.on("keyup",".txtUrl",(function(){var e=o.find(".dd-handle.selected").closest("li"),n=a(this).val();e.attr("data-url",n),e.data("url",n)})),o.on("change",".selHideDepartments",(function(){var e=o.find(".dd-handle.selected").closest("li"),n=a(this).select2("val");e.attr("data-hidden-dpts",n)})),o.on("change",".selectedDash",(function(){var e=o.find(".dd-handle.selected").closest("li"),n=a(this).select2("val");e.attr("data-dash-id",n),e.data("dash-id",n)})),o.on("change",".selectedTaskLog",(function(){var e=o.find(".dd-handle.selected").closest("li"),n=a(this).select2("val"),t=a(this).select2("data").hasParams;e.attr("data-tasklog-id",n),e.data("tasklog-id",n),e.attr("data-tasklog-has-params",t),e.data("tasklog-has-params",t)})),o.find(".selectAction").on("change",(function(e){var n=o.find(".dd-handle.selected").closest("li"),t=a(e.currentTarget).select2("val");o.find('[class*="Block"]').hide(),o.find(".".concat(t,"Block")).show(),n.attr("data-action",t),n.data("action",t),"openDash"===t?(o.find(".selectedDash").attr("disabled",!1),o.find(".selectedTaskLog").attr("disabled",!0)):"openTaskLog"===t?(o.find(".selectedDash").attr("disabled",!0),o.find(".selectedTaskLog").attr("disabled",!1)):(o.find(".selectedDash").attr("disabled",!0),o.find(".selectedTaskLog").attr("disabled",!0))})),o.find('input[type="checkbox"]').on("ifToggled",(function(e){var n=o.find(".dd-handle.selected").closest("li");setTimeout((function(){var t=a(e.currentTarget).is(":checked");n.attr("data-blank-target",t),n.data("blank-target",t)}),200)})),a("#main-modal .modal-footer button").click((function(){var e=!0;return t.callback&&(t.itemProperties.menuDefinition=l.$el.find(".dd").nestable("serialize"),!1===t.callback.call(this,a(this).attr("data-code"),t.itemProperties)&&(e=!1)),e&&(a("#main-modal").off("shown"),a("#main-modal").modal("hide")),!1})),a("#main-modal").on("show.bs.modal",(function(){if(0===a("#main-modal:visible").length){var e=100014+10*a(".modal:visible").length;a(this).css("z-index",e),setTimeout((function(){a(".modal-backdrop").not(".modal-stack").css("z-index",e-10).addClass("modal-stack")}),0),t.hasOwnProperty("onLoad")&&t.onLoad(a("#main-modal")),!0!==t.okOnEnter&&void 0!==t.okOnEnter||a("#main-modal").keyup((function(e){13==e.keyCode&&a("#main-modal button.btn-primary").click()}))}})),a("#main-modal").on("hidden.bs.modal",(function(){a("#main-modal").off("hidden"),t.hasOwnProperty("onClose")&&t.onClose(a("#main-modal")),a("#main-modal").remove()}));var r=null;t.backdrop&&(r={backdrop:"static",keyboard:!1}),a("#main-modal").modal(r)}},populateForm:function(e,n){var t=e.attr("data-title"),l=e.attr("data-subtitle"),a=e.attr("data-icon"),i=e.attr("data-action"),o=e.attr("data-dash-id"),s=e.attr("data-tasklog-id"),c=e.attr("data-url"),r=e.attr("data-blank-target"),d=e.attr("data-hidden-dpts");n.find(".txtTitle").val(t),n.find(".txtSubtitle").val(l),n.find(".txtIcon").val(a),n.find(".txtUrl").val(c),n.find(".selectAction").select2("val",i),n.find(".selectedDash").select2("val",o),n.find(".selectedTaskLog").select2("val",s),n.find(".selHideDepartments").select2("val",d?d.split(","):[]),"true"==r?(n.find('input[name="chkBlank"]').iCheck("check"),n.find('input[name="chkBlank"]').iCheck("update")):(n.find('input[name="chkBlank"]').iCheck("uncheck"),n.find('input[name="chkBlank"]').iCheck("update")),e.children().first().is(":button")&&(n.find(".selectAction").val("hasSubmenu"),n.find(".selectedDash").val("0")),n.find(".selectAction").trigger("change")},loadSelectLists:function(e){(0,s.haveAccess)("view_department")&&Promise.resolve().then((function(){var n=[t(220)];(function(n){(new n).getDepartments((function(n){var t=e.find("select.selHideDepartments");a.each(n,(function(e,n){t.append(a("<option />").val(n.id).text(n.name))})),t.select2({width:350,escapeMarkup:function(e){return e}})}),(function(){}))}).apply(null,n)})).catch(t.oe),Promise.resolve().then((function(){(function(n){var l=[t(763)];(function(t){(new t).allMyDashboards(null,(function(t){var l=e.find("select.selectedDash"),i=n.groupBy(t,(function(e){return e.owner==__currentSession.userCompanyId?"My Interfaces":"Shared Interfaces"})),o={};Object.keys(i).sort().forEach((function(e){o[e]=i[e]})),l.append(a("<option />").val("0").text("Select an interface"));var s=function(e){var n=a("<optgroup />").attr("label",e);a.each(o[e],(function(e,t){var l=t.uuid?t.uuid:t.dashItemId;n.append(a("<option />").val(l).text(t.name))})),l.append(n)};for(var c in o)s(c);l.select2({width:"90%",escapeMarkup:function(e){return e}})}),(function(){}))}).apply(null,l)}).call(this,t(221))})).catch(t.oe),(0,s.haveAccess)("view_periodictasklog")&&t.e(284).then((function(){var n=[t(739)];(function(n){(new n).list((function(n){var t=n.map((function(e){return e.text=e.text||e.name,e}));t.unshift({id:0,text:"Select task",hasParam:!1});var l=e.find("div.selectedTaskLog");l.select2({data:t,width:250,escapeMarkup:function(e){return e}}),l.select2("val",0)}),(function(){}))}).apply(null,n)})).catch(t.oe),e.find("select.selectAction").select2({width:"90%"})}});return n}.apply(n,i))||(e.exports=o)}).call(this,t(219),t(1))},2707:function(e,n,t){var l=t(2708);"string"==typeof l&&(l=[[e.i,l,""]]);var a={hmr:!0,transform:void 0,insertInto:void 0};t(224)(l,a);l.locals&&(e.exports=l.locals)},2708:function(e,n,t){(n=e.exports=t(2)(!1)).i(t(2709),""),n.push([e.i,"",""])},2710:function(e,n,t){var l=t(670);function a(e){return e&&(e.__esModule?e.default:e)}e.exports=(l.default||l).template({1:function(e,n,t,l,a){return'                  <li class="">\n                    <a href="#drawMenuTab3" class="drawMenuTab3 disabled" data-toggle="tab">Restriction rules</a>\n                  </li>\n'},3:function(e,n,t,l,a){return" selected "},5:function(e,n,t,l,a){return" selected\n                              "},7:function(e,n,t,l,a){return" checked "},9:function(e,n,t,l,a){return'                      <div class="check-line nodisplay openTaskLogBlock">\n                        <div class="row">\n                          <div class="col-sm-5">\n                            <div class="selectedTaskLog" style="margin-left: 25px;"></div>\n                          </div>\n                        </div>\n                      </div>\n'},11:function(e,n,t,l,a){return'                  <div class="tab-pane" id="drawMenuTab3">\n                    <div class="col-sm-12 form-vertical itemSettings">\n                      <div class="form-group">\n                        <label for="textfield" class="control-label col-sm-12 nopadding">Hide by department</label>\n                        <select class="selHideDepartments" data="hideDepartments" multiple="multiple">\n                        </select>\n                      </div>\n                    </div>\n                  </div>\n'},13:function(e,n,t,l,a){var i=e.lambda,o=e.escapeExpression,s=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'        <button class="btn btn-'+o(i(null!=n?s(n,"css"):n,n))+'" data-code="'+o(i(null!=n?s(n,"code"):n,n))+'" data-dismiss="modal" aria-hidden="true">'+o(i(null!=n?s(n,"title"):n,n))+"</button>\n"},compiler:[8,">= 4.3.0"],main:function(e,n,l,i,o){var s,c=e.lambda,r=e.escapeExpression,d=null!=n?n:e.nullContext||{},u=e.lookupProperty||function(e,n){if(Object.prototype.hasOwnProperty.call(e,n))return e[n]};return'<div id="main-modal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"\n  style="display: none;">\n  <div class="modal-dialog '+r(c(null!=n?u(n,"modalClass"):n,n))+'">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button>\n        <h4 class="modal-title" id="myModalLabel">'+r(c(null!=n?u(n,"title"):n,n))+'</h4>\n      </div>\n\n      <div class="modal-body" style="overflow-y:auto; overflow-x: hidden;">\n\n        <div class="row">\n          <div class="col-sm-5">\n            <div class="col-sm-12">\n              <button class="btn btn-small btnAddItem">Add item</button>\n            </div>\n            <div class="col-sm-12">\n              <div class="dd">\n                <ol class="dd-list">\n\n                </ol>\n              </div>\n            </div>\n          </div>\n\n          <div class="col-sm-7">\n            <div class="box">\n              <div class="box-title">\n                <ul class="tabs tabs-left">\n                  <li class="active">\n                    <a href="#drawMenuTab1" class="drawMenuTab1" data-toggle="tab">General properties</a>\n                  </li>\n                  <li class="">\n                    <a href="#drawMenuTab2" class="drawMenuTab2 disabled" data-toggle="tab">Option properties</a>\n                  </li>\n'+(null!=(s=a(t(681)).call(d,"view_department",{name:"haveAccess",hash:{},fn:e.program(1,o,0),inverse:e.noop,data:o,loc:{start:{line:36,column:18},end:{line:40,column:33}}}))?s:"")+'                </ul>\n              </div>\n              <div class="box-content">\n                <div class="tab-content">\n                  <div class="tab-pane active" id="drawMenuTab1">\n\n                    <div class="col-sm-12 form-vertical generalSettings">\n                      <h4 style="margin-top: 0;">Root title</h4>\n                      <div class="row">\n                        <div class="col-sm-6">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Title</label> <br>\n                            <input type="text" class="form-control txtMenuTitle"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"menuTitle"):s,n))+'" />\n                          </div>\n                        </div>\n                        <div class="col-sm-3">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Size (px)</label>\n                            <input type="text" class="form-control txtMenuTitleSize"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"menuTitleSize"):s,n))+'" placeholder="Ex: 15px" />\n                          </div>\n                        </div>\n                        <div class="col-sm-3">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Color</label> <br>\n                            <input type="text" class="form-control spectrum-colors txtMenuTitleColor"\n                              data-key="menu-title-color" value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"menuTitleColor"):s,n))+'" />\n                          </div>\n                        </div>\n                      </div>\n                      <h4 style="margin-top: 0;">Menu options</h4>\n                      <div class="row">\n                        <div class="col-sm-6">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Items per row</label> <br>\n                            <input type="text" class="form-control txtItemsPerRow"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"itemsPerRow"):s,n))+'" />\n                          </div>\n                        </div>\n                        <div class="col-sm-6">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Items align</label>\n                            <select name="select" class="form-control selItemsAlign" style="width: 100%;">\n                              <option value="leftAlign">Left</option>\n                              <option value="centerAlign">Center</option>\n                              <option value="rightAlign">Rigth</option>\n                            </select>\n                          </div>\n                        </div>\n                      </div>\n\n                      <div class="row">\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Title/sub align</label>\n                            <select name="select" class="form-control selTextAlign" style="width: 100%;">\n                              <option value="leftAlign">Left</option>\n                              <option value="centerAlign">Center</option>\n                              <option value="rightAlign">Rigth</option>\n                            </select>\n                          </div>\n                        </div>\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Title size (px)</label>\n                            <input type="text" class="form-control txtTitleSize"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"titleSize"):s,n))+'" placeholder="Ex: 22px" />\n                          </div>\n                        </div>\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Title top margin (px)</label>\n                            <input type="text" class="form-control txtTitleMargin"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"titleMargin"):s,n))+'" placeholder="Ex: 0px" />\n                          </div>\n                        </div>\n                      </div>\n\n                      <div class="row">\n                        <div class="col-sm-4">\n\n                        </div>\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Subtitle size (px)</label>\n                            <input type="text" class="form-control txtSubtitleSize"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"subtitleSize"):s,n))+'" placeholder="Ex: 15px" />\n                          </div>\n                        </div>\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Subtitle top margin (px)</label>\n                            <input type="text" class="form-control txtSubtitleMargin"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"subtitleMargin"):s,n))+'" placeholder="Ex: 15px" />\n                          </div>\n                        </div>\n                      </div>\n\n\n                      <div class="row">\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Background color</label> <br>\n                            <input type="text" class="form-control spectrum-colors txtBgColor" data-key="bg-color"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"backgroundColor"):s,n))+'" />\n                          </div>\n                        </div>\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Hover color</label> <br>\n                            <input type="text" class="form-control spectrum-colors txtHoverColor" data-key="hover-color"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"hoverBackgroundColor"):s,n))+'" />\n                          </div>\n                        </div>\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Text color</label> <br>\n                            <input type="text" class="form-control spectrum-colors txtColor" data-key="text-color"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"textColor"):s,n))+'" />\n                          </div>\n                        </div>\n                      </div>\n\n                      <div class="row">\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Icon size (px/em)</label> <br>\n                            <input type="text" class="form-control txtIconSize"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"iconSize"):s,n))+'" />\n                          </div>\n                        </div>\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Icon margin top (px/%)</label> <br>\n                            <input type="text" class="form-control txtIconMarginTop"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"iconMarginTop"):s,n))+'" />\n                          </div>\n                        </div>\n                        <div class="col-sm-4">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Icon color</label> <br>\n                            <input type="text" class="form-control spectrum-colors txtIconColor" data-key="icon-color"\n                              value="'+r(c(null!=(s=null!=(s=null!=n?u(n,"itemProperties"):n)?u(s,"generalSettings"):s)?u(s,"iconColor"):s,n))+'" />\n                          </div>\n                        </div>\n                        <div class="col-sm-4">\n\n                        </div>\n                      </div>\n\n                    </div>\n                  </div>\n\n                  \x3c!-- TAB 2 --\x3e\n                  <div class="tab-pane" id="drawMenuTab2">\n                    <div class="col-sm-12 form-vertical itemSettings">\n                      <div class="form-group">\n                        <label for="textfield" class="control-label">Title</label>\n                        <input type="text" class="form-control txtTitle" data="title" />\n                      </div>\n                      <div class="form-group">\n                        <label for="textfield" class="control-label">Subtitle</label>\n                        <input type="text" class="form-control txtSubtitle" data="subtitle" />\n                      </div>\n                      <div class="row">\n                        <div class="col-sm-6">\n                          <div class="form-group">\n                            <label for="textfield" class="control-label">Icon</label>\n                            <input type="text" class="form-control txtIcon" data="icon" placeholder="Ex: fa fa-plus" />\n                          </div>\n                        </div>\n                      </div>\n                      <label for="textfield" class="control-label">Action</label>\n\n                      <div class="row" style="margin-bottom: 15px;">\n                        <div class="col-sm-6">\n                          <select class="selectAction" style="margin-left: 25px;">\n                            <option value="noAction">None/Disabled</option>\n                            <option value="hasSubmenu" '+(null!=(s=a(t(669)).call(d,null!=n?u(n,"hasSubmenu"):n,"==",!0,{name:"ifCond",hash:{},fn:e.program(3,o,0),inverse:e.noop,data:o,loc:{start:{line:220,column:55},end:{line:220,column:113}}}))?s:"")+'>Open\n                              submenu</option>\n                            <option value="openDiagram" '+(null!=(s=a(t(669)).call(d,null!=n?u(n,"action"):n,"==","openDiagram",{name:"ifCond",hash:{},fn:e.program(3,o,0),inverse:e.noop,data:o,loc:{start:{line:222,column:56},end:{line:222,column:119}}}))?s:"")+'>\n                              Open Diagram</option>\n                            <option value="openFileManager" '+(null!=(s=a(t(669)).call(d,null!=n?u(n,"action"):n,"==","openFileManager",{name:"ifCond",hash:{},fn:e.program(5,o,0),inverse:e.noop,data:o,loc:{start:{line:224,column:60},end:{line:225,column:41}}}))?s:"")+'>Open File Manager</option>\n                            <option value="openDash" '+(null!=(s=a(t(669)).call(d,null!=n?u(n,"action"):n,"==","openDash",{name:"ifCond",hash:{},fn:e.program(3,o,0),inverse:e.noop,data:o,loc:{start:{line:226,column:53},end:{line:226,column:113}}}))?s:"")+'>Open a\n                              interface</option>\n                            <option value="openTaskLog" '+(null!=(s=a(t(669)).call(d,null!=n?u(n,"action"):n,"==","openTaskLog",{name:"ifCond",hash:{},fn:e.program(3,o,0),inverse:e.noop,data:o,loc:{start:{line:228,column:56},end:{line:228,column:119}}}))?s:"")+'>\n                              Open Task log</option>\n                            <option value="openUrl" '+(null!=(s=a(t(669)).call(d,null!=n?u(n,"action"):n,"==","openUrl",{name:"ifCond",hash:{},fn:e.program(3,o,0),inverse:e.noop,data:o,loc:{start:{line:230,column:52},end:{line:230,column:111}}}))?s:"")+'>Open URL\n                            </option>\n                          </select>\n                        </div>\n                      </div>\n\n                      \x3c!-- Open interface --\x3e\n                      <div class="check-line nodisplay openDashBlock">\n                        <div class="row">\n                          <div class="col-sm-6">\n                            <select class="selectedDash" style="margin-left: 25px;" disabled="disabled"></select>\n                          </div>\n                          <div class="col-sm-6">\n                            <div class="check-line">\n                              <input type="checkbox" class=\'icheck-me to\' name="chkBlank" data-skin="square"\n                                data-color="blue" '+(null!=(s=a(t(669)).call(d,null!=n?u(n,"blankTarget"):n,"==","true",{name:"ifCond",hash:{},fn:e.program(7,o,0),inverse:e.noop,data:o,loc:{start:{line:245,column:50},end:{line:245,column:110}}}))?s:"")+" />\n                              <label class='inline'>Open in a new tab</label>\n                            </div>\n                          </div>\n                        </div>\n                      </div>\n\n                      \x3c!-- Open task log --\x3e\n"+(null!=(s=a(t(681)).call(d,"view_periodictasklog",{name:"haveAccess",hash:{},fn:e.program(9,o,0),inverse:e.noop,data:o,loc:{start:{line:253,column:22},end:{line:261,column:37}}}))?s:"")+'\n                      \x3c!-- Open URL --\x3e\n                      <div class="check-line nodisplay openUrlBlock">\n                        <div class="row">\n                          <div class="col-sm-6">\n                            <input type="text" class="form-control txtUrl" style="margin-left: 25px;" />\n                          </div>\n                          <div class="col-sm-6">\n                            <div class="check-line">\n                              <input type="checkbox" class=\'icheck-me to\' name="chkBlank" data-skin="square"\n                                data-color="blue" '+(null!=(s=a(t(669)).call(d,null!=n?u(n,"blankTarget"):n,"==","true",{name:"ifCond",hash:{},fn:e.program(7,o,0),inverse:e.noop,data:o,loc:{start:{line:272,column:50},end:{line:272,column:110}}}))?s:"")+" />\n                              <label class='inline'>Open in a new tab</label>\n                            </div>\n                          </div>\n                        </div>\n                      </div>\n\n                    </div>\n                  </div>\n                  \x3c!-- END TAB 2 --\x3e\n\n                  \x3c!-- TAB 3 --\x3e\n"+(null!=(s=a(t(681)).call(d,"view_department",{name:"haveAccess",hash:{},fn:e.program(11,o,0),inverse:e.noop,data:o,loc:{start:{line:284,column:18},end:{line:294,column:33}}}))?s:"")+'                  \x3c!-- END TAB 3 --\x3e\n\n                </div>\n              </div>\n            </div>\n          </div>\n\n        </div>\n\n      </div>\n      <div class="modal-footer">\n'+(null!=(s=u(l,"each").call(d,null!=n?u(n,"buttons"):n,{name:"each",hash:{},fn:e.program(13,o,0),inverse:e.noop,data:o,loc:{start:{line:306,column:8},end:{line:308,column:17}}}))?s:"")+"      </div>\n    </div>\n  </div>\n</div>"},useData:!0})}}]);