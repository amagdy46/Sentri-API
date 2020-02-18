(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-55ecc1ec"],{"0360":function(t,e,s){"use strict";s.r(e);var a=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{attrs:{id:"dashboard-analytics"}},[s("div",{staticClass:"vx-row"},[s("div",{staticClass:"vx-col w-full lg:w-1/3 mb-base"},[s("vx-card",{attrs:{title:"Orders"}},[s("template",{slot:"actions"}),s("div",{attrs:{slot:"no-body"},slot:"no-body"},[s("vue-apex-charts",{attrs:{type:"radialBar",height:"300",options:t.analyticsData.productOrdersRadialBar.chartOptions,series:t.series}})],1),s("ul",[s("li",{staticClass:"flex mb-3 justify-between"},[s("span",{staticClass:"flex items-center"},[s("span",{staticClass:"inline-block h-4 w-4 rounded-full mr-2 bg-white border-3 border-solid border-primary"}),s("span",{staticClass:"font-semibold"},[t._v("Pending")])]),s("span",[s("animated-number",{attrs:{round:"1",value:t.orders.pending.length}})],1)]),s("li",{staticClass:"flex mb-3 justify-between"},[s("span",{staticClass:"flex items-center"},[s("span",{staticClass:"inline-block h-4 w-4 rounded-full mr-2 bg-white border-3 border-solid border-warning"}),s("span",{staticClass:"font-semibold"},[t._v("Out")])]),s("span",[s("animated-number",{attrs:{round:"1",value:t.orders.out.length}})],1)]),s("li",{staticClass:"flex mb-3 justify-between"},[s("span",{staticClass:"flex items-center"},[s("span",{staticClass:"inline-block h-4 w-4 rounded-full mr-2 bg-white border-3 border-solid border-danger"}),s("span",{staticClass:"font-semibold"},[t._v("Canceled")])]),s("span",[s("animated-number",{attrs:{round:"1",value:t.orders.canceled.length}})],1)]),s("li",{staticClass:"flex mb-3 justify-between"},[s("span",{staticClass:"flex items-center"},[s("span",{staticClass:"inline-block h-4 w-4 rounded-full mr-2 bg-white border-3 border-solid border-success"}),s("span",{staticClass:"font-semibold"},[t._v("Delivered")])]),s("span",[s("animated-number",{attrs:{round:"1",value:t.orders.delivered.length}})],1)])])],2)],1),s("div",{staticClass:"vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4 mb-base"},[s("statistics-card-line",{attrs:{icon:"UsersIcon",statistic:t.users,statisticTitle:"Subscribers Gained",chartData:t.subscribersGained.series,type:"area"}}),s("statistics-card-line",{staticClass:"mt-5",attrs:{icon:"ShoppingBagIcon",statistic:t.products.length,statisticTitle:"Orders Received",chartData:t.subscribersGained.series,color:"warning",type:"area"}})],1),s("div",{staticClass:"vx-col w-full sm:w-1/2 md:w-1/2 lg:w-1/4 xl:w-1/4 mb-base"},[s("vx-card",{attrs:{title:"Choose Date"}},[s("flat-pickr",{attrs:{config:t.configFromdateTimePicker,placeholder:"From Date"},on:{"on-change":t.onFromChange},model:{value:t.fromDate,callback:function(e){t.fromDate=e},expression:"fromDate"}}),s("flat-pickr",{attrs:{config:t.configTodateTimePicker,placeholder:"To Date"},on:{"on-change":t.onToChange},model:{value:t.toDate,callback:function(e){t.toDate=e},expression:"toDate"}})],1)],1)])])},r=[],i=s("044d"),n=s.n(i),o=s("1321"),c=s.n(o),l=s("c38f"),d=s.n(l),u=(s("0952"),s("43ca")),f=s("da24"),h={data:function(){return{fromDate:"2020-01-01",toDate:new Date,configFromdateTimePicker:{minDate:null,maxDate:null},configTodateTimePicker:{minDate:null},checkpointReward:{},subscribersGained:{},ordersRecevied:{},salesBarSession:{},supportTracker:{},productsOrder:{},salesRadar:{},analyticsData:f["a"],dispatchedOrders:[]}},components:{AnimatedNumber:n.a,VueApexCharts:c.a,StatisticsCardLine:u["a"],flatPickr:d.a},created:function(){var t=this;this.$http.get("/api/card/card-statistics/subscribers").then((function(e){t.subscribersGained=e.data})).catch((function(t){console.log(t)})),this.$http.get("/api/card/card-analytics/products-orders").then((function(e){t.productsOrder=e.data})).catch((function(t){console.log(t)}))},computed:{users:function(){return this.$store.state.dataList.users},products:function(){var t=this;return this.$store.state.dataList.products.filter((function(e){return e.time>=Date.parse(t.fromDate)&&e.time<=Date.parse(t.toDate)}))},orders:function(){var t=this.products;return{pending:t.filter((function(t){return"Pending"==t.status})),out:t.filter((function(t){return"Out"==t.status})),canceled:t.filter((function(t){return"Canceled"==t.status})),delivered:t.filter((function(t){return"Delivered"==t.status}))}},series:function(){var t=this.orders.pending.length,e=this.orders.out.length,s=this.orders.canceled.length,a=this.orders.delivered.length,r=t+e+s+a,i=Math.round(a/r*100),n=Math.round(e/r*100),o=Math.round(t/r*100),c=Math.round(s/r*100);return[i,c,n,o]}},methods:{onFromChange:function(t,e){this.$set(this.configTodateTimePicker,"minDate",e)},onToChange:function(t,e){this.$set(this.configFromdateTimePicker,"maxDate",e)}}},m=h,b=(s("47f6"),s("2877")),p=Object(b["a"])(m,a,r,!1,null,null,null);e["default"]=p.exports},"37c0":function(t,e,s){},"47f6":function(t,e,s){"use strict";var a=s("37c0"),r=s.n(a);r.a}}]);
//# sourceMappingURL=chunk-55ecc1ec.9426fc6d.js.map