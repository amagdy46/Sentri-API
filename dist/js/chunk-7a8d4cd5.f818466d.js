(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-7a8d4cd5"],{2471:function(t,e,a){},"4c46":function(t,e,a){"use strict";var s=a("b5e8"),r=a.n(s);r.a},"5fad":function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"data-list-container",attrs:{id:"data-list-list-view"}},[a("data-view-sidebar",{attrs:{isSidebarActive:t.addNewDataSidebar,data:t.sidebarData},on:{closeSidebar:t.toggleDataSidebar}}),a("vs-table",{ref:"table",attrs:{multiple:"",pagination:"","max-items":t.itemsPerPage,search:"",data:t.products},scopedSlots:t._u([{key:"default",fn:function(e){var s=e.data;return[a("tbody",t._l(s,(function(e,s){return a("vs-tr",{key:s,attrs:{data:e}},[a("vs-td",[a("p",{staticClass:"product-phone"},[t._v("\n              "+t._s(e.time.getDate())+"-"+t._s(e.time.getMonth()+1)+"-"+t._s(e.time.getFullYear())+"\n              T "+t._s(e.time.getHours())+":"+t._s(e.time.getMinutes())+"\n            ")])]),a("vs-td",[a("p",{staticClass:"product-phone"},[t._v(t._s(e.number))])]),a("vs-td",[a("p",{staticClass:"product-name font-medium truncate"},[t._v("\n              "+t._s(e.customer.name)+"\n            ")])]),a("vs-td",[a("p",{staticClass:"product-phone"},[t._v(t._s(e.customer.phone_number))])]),a("vs-td",[a("p",{staticClass:"product-address"},[t._v(t._s(e.customer.address))])]),a("vs-td",[a("p",{staticClass:"product-order"},[t._v(t._s(e.items))])]),a("vs-td",[a("vs-chip",{staticClass:"product-order-status",attrs:{color:t.getOrderStatusColor(e.status)}},[t._v(t._s(e.status))])],1),a("vs-td",[a("p",{staticClass:"product-price"},[t._v("L.E"+t._s(e.total))])]),a("vs-td",{staticClass:"whitespace-no-wrap"},[a("feather-icon",{attrs:{icon:"EditIcon",svgClasses:"w-5 h-5 hover:text-primary stroke-current"},on:{click:function(a){return a.stopPropagation(),t.editData(e)}}})],1)],1)})),1)]}}]),model:{value:t.selected,callback:function(e){t.selected=e},expression:"selected"}},[a("div",{staticClass:"flex flex-wrap-reverse items-center flex-grow justify-between",attrs:{slot:"header"},slot:"header"},[a("vs-spacer"),a("vs-dropdown",{staticClass:"cursor-pointer mb-4 mr-4 items-per-page-handler",attrs:{"vs-trigger-click":""}},[a("div",{staticClass:"p-4 border border-solid d-theme-border-grey-light rounded-full d-theme-dark-bg cursor-pointer flex items-center justify-between font-medium"},[a("span",{staticClass:"mr-2"},[t._v(t._s(t.currentPage*t.itemsPerPage-(t.itemsPerPage-1))+" -\n            "+t._s(t.products.length-t.currentPage*t.itemsPerPage>0?t.currentPage*t.itemsPerPage:t.products.length)+"\n            of "+t._s(t.queriedItems))]),a("feather-icon",{attrs:{icon:"ChevronDownIcon",svgClasses:"h-4 w-4"}})],1),a("vs-dropdown-menu",[a("vs-dropdown-item",{on:{click:function(e){t.itemsPerPage=5}}},[a("span",[t._v("5 per View")])]),a("vs-dropdown-item",{on:{click:function(e){t.itemsPerPage=10}}},[a("span",[t._v("10 per View")])]),a("vs-dropdown-item",{on:{click:function(e){t.itemsPerPage=15}}},[a("span",[t._v("15 per View")])]),a("vs-dropdown-item",{on:{click:function(e){t.itemsPerPage=20}}},[a("span",[t._v("20 per View")])])],1)],1)],1),a("template",{slot:"thead"},[a("vs-th",{attrs:{"sort-key":"time"}},[t._v("TIMESTAMP")]),a("vs-th",{attrs:{"sort-key":"number"}},[t._v("NUMBER")]),a("vs-th",{attrs:{"sort-key":"user.name"}},[t._v("NAME")]),a("vs-th",{attrs:{"sort-key":"phone_number"}},[t._v("PHONE")]),a("vs-th",{attrs:{"sort-key":"address"}},[t._v("ADDRESS")]),a("vs-th",{attrs:{"sort-key":"items"}},[t._v("ORDER")]),a("vs-th",{attrs:{"sort-key":"status"}},[t._v("STATUS")]),a("vs-th",{attrs:{"sort-key":"price"}},[t._v("PRICE")]),a("vs-th",[t._v("Action")])],1)],2)],1)},r=[],i=(a("96cf"),a("3b8d")),n=a("6dd9"),o={components:{DataViewSidebar:n["a"]},data:function(){return{status:[{name:"Pending"},{name:"Out"},{name:"Canceled"},{name:"Delivered"}],selected:[],itemsPerPage:5,isMounted:!1,addNewDataSidebar:!1,sidebarData:{}}},computed:{currentPage:function(){return this.isMounted?(this.$vs.loading.close(),this.$refs.table.currentx):0},products:function(){return this.$store.state.dataList.products},queriedItems:function(){return this.$refs.table?this.$refs.table.queriedResults.length:this.products.length}},sockets:{connect:function(){console.log("Dtlst Socket connected")},order:function(t){var e=JSON.parse(t);this.$store.dispatch("dataList/addItem",e[0])}},methods:{addNewData:function(){this.sidebarData={},this.toggleDataSidebar(!0)},deleteData:function(t){this.$store.dispatch("dataList/removeItem",t).catch((function(t){console.error(t)}))},editData:function(t){this.sidebarData=t,this.toggleDataSidebar(!0),console.log(this.products)},getOrderStatusColor:function(t){return"Out"==t?"warning":"Delivered"==t?"success":"Canceled"==t?"danger":"primary"},toggleDataSidebar:function(){var t=arguments.length>0&&void 0!==arguments[0]&&arguments[0];this.addNewDataSidebar=t}},created:function(){var t=Object(i["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:case"end":return t.stop()}}),t)})));function e(){return t.apply(this,arguments)}return e}(),mounted:function(){this.isMounted=!0}},c=o,d=(a("9153"),a("2877")),l=Object(d["a"])(c,s,r,!1,null,null,null);e["default"]=l.exports},"6dd9":function(t,e,a){"use strict";var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("vs-sidebar",{staticClass:"add-new-data-sidebar items-no-padding",attrs:{"click-not-close":"","position-right":"",parent:"body","default-index":"1",color:"primary",spacer:""},model:{value:t.isSidebarActiveLocal,callback:function(e){t.isSidebarActiveLocal=e},expression:"isSidebarActiveLocal"}},[a("div",{staticClass:"mt-6 flex items-center justify-between px-6"},[a("h4",[t._v("\n      "+t._s(0===Object.entries(this.data).length?"ADD NEW":"UPDATE")+" ITEM\n    ")]),a("feather-icon",{staticClass:"cursor-pointer",attrs:{icon:"XIcon"},on:{click:function(e){e.stopPropagation(),t.isSidebarActiveLocal=!1}}})],1),a("vs-divider",{staticClass:"mb-0"}),a("VuePerfectScrollbar",{key:t.$vs.rtl,staticClass:"scroll-area--data-list-add-new",attrs:{settings:t.settings}},[a("div",{staticClass:"p-6"},[a("vs-input",{directives:[{name:"validate",rawName:"v-validate",value:"required",expression:"'required'"}],staticClass:"mt-5 w-full",attrs:{disabled:"",label:"Number",name:"number"},model:{value:t.dataNumber,callback:function(e){t.dataNumber=e},expression:"dataNumber"}}),a("span",{directives:[{name:"show",rawName:"v-show",value:t.errors.has("item-name"),expression:"errors.has('item-name')"}],staticClass:"text-danger text-sm"},[t._v(t._s(t.errors.first("item-name")))]),a("vs-select",{directives:[{name:"validate",rawName:"v-validate",value:"required",expression:"'required'"}],staticClass:"mt-5 w-full",attrs:{label:"Stauts",name:"item-Status"},model:{value:t.dataStatus,callback:function(e){t.dataStatus=e},expression:"dataStatus"}},t._l(t.status_choices,(function(t){return a("vs-select-item",{key:t.value,attrs:{value:t.value,text:t.text}})})),1),a("span",{directives:[{name:"show",rawName:"v-show",value:t.errors.has("item-category"),expression:"errors.has('item-category')"}],staticClass:"text-danger text-sm"},[t._v(t._s(t.errors.first("item-category")))]),a("vs-input",{directives:[{name:"validate",rawName:"v-validate",value:{required:!0,regex:/\d+(\.\d+)?$/},expression:"{ required: true, regex: /\\d+(\\.\\d+)?$/ }"}],staticClass:"mt-5 w-full",attrs:{disabled:"","icon-pack":"feather",icon:"icon-credit-card",label:"Price",name:"item-price"},model:{value:t.dataPrice,callback:function(e){t.dataPrice=e},expression:"dataPrice"}})],1)]),a("div",{staticClass:"flex flex-wrap items-center p-6",attrs:{slot:"footer"},slot:"footer"},[a("vs-button",{staticClass:"mr-6",on:{click:t.submitData}},[t._v("Submit")]),a("vs-button",{attrs:{type:"border",color:"danger"},on:{click:function(e){t.isSidebarActiveLocal=!1}}},[t._v("Cancel")])],1)],1)},r=[],i=(a("ac6a"),a("ffc1"),a("9d63")),n=a.n(i),o={props:{isSidebarActive:{type:Boolean,required:!0},data:{type:Object,default:function(){}}},watch:{isSidebarActive:function(t){t&&(0===Object.entries(this.data).length?(this.initValues(),this.$validator.reset()):(console.log(this.data),this.dataOrder=this.data.items,this.dataStatus=this.data.status,this.dataPrice=this.data.total,this.dataNumber=this.data.number))}},data:function(){return{dataOrder:"",dataStatus:"",dataPrice:0,dataNumber:0,status_choices:[{text:"Pending",value:"Pending"},{text:"Out",value:"Out"},{text:"Canceled",value:"Canceled"},{text:"Delivered",value:"Delivered"}],settings:{maxScrollbarLength:60,wheelSpeed:.6}}},computed:{isSidebarActiveLocal:{get:function(){return this.isSidebarActive},set:function(t){t||this.$emit("closeSidebar")}},isFormValid:function(){return!this.errors.any()&&this.dataName&&this.dataCategory&&this.dataPrice>0}},methods:{initValues:function(){this.dataOrder="",this.dataStatus="Pending",this.dataPrice=0},submitData:function(){var t={number:this.dataNumber,status:this.dataStatus};console.log(t.number),this.$store.dispatch("dataList/updateItem",t).catch((function(t){console.error(t)})),this.$emit("closeSidebar")}},components:{VuePerfectScrollbar:n.a}},c=o,d=(a("4c46"),a("2877")),l=Object(d["a"])(c,s,r,!1,null,"8d0d363c",null);e["a"]=l.exports},9153:function(t,e,a){"use strict";var s=a("2471"),r=a.n(s);r.a},b5e8:function(t,e,a){}}]);
//# sourceMappingURL=chunk-7a8d4cd5.f818466d.js.map