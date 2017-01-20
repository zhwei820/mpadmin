import Vue from 'vue'
import ElementUI from 'element-ui'
Vue.use(ElementUI)

import VueResource from 'vue-resource';
Vue.use(VueResource);

Vue.http.interceptors.push((request, next) => {
    var Authorization = localStorage.getItem("Authorization");
    console.log(Authorization);
    
  if(Authorization){
      request.headers.set('Authorization', Authorization);
  }
  next();
});




var addEvent = function (elem, event, fn) {
    if (elem.addEventListener) {
        elem.addEventListener(event, fn, false);
    } else if (elem.attachEvent) {
        elem.attachEvent('on' + event, fn);
    } else {
        elem['on' + event] = fn;
    }
}


var echo = function (value) {　　
    console.log(value)
}


function getType(o) {
    var _t;
    return ((_t = typeof o) == "object" ? o == null && "null" || Object.prototype.toString.call(o).slice(8, -1) : _t).toLowerCase();
}

function extend(destination, source) {
    for (var p in source) {
        if (getType(source[p]) == "array" || getType(source[p]) == "object") {
            destination[p] = getType(source[p]) == "array" ? [] : {};
            arguments.callee(destination[p], source[p]);
        } else {
            destination[p] = source[p];
        }
    }
}
// var test={a:"ss",b:"dd",c:{d:"css",e:"cdd"}};
// var test1={};
// extend(test1,test);


function export_excel(rows, rowKeys, charset, type) {
    var tpl = '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:{{type}}" xmlns="http://www.w3.org/TR/REC-html40">';
    tpl += '<head><meta charset="{{charset}}" /><!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>';
    tpl += '表格1</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]-->';
    tpl += '</head><body><table border="1 solid black">{{table}}</table></body></html>';

    var office = '';
    var maph = [
        ['<thead><tr>', '</tr></thead>'],
        ['<tbody><tr>', '</tr></tbody>'],
        ['<tr>', '</tr>']
    ];
    var mapb = [
        ['<th>', '</th>'],
        ['<td style="vnd.ms-excel.numberformat:@">', '</td>']
    ];
    var flag = 0;
    var com = 1 - flag;

    for (var ii = 0; ii < rows.length; ii++) {
        flag = ii > com ? 2 : flag;
        office += maph[flag][0];
        for (var jj in rowKeys) {
            office += mapb[+!!flag][0] + rows[ii][rowKeys[jj]] + mapb[+!!flag][1];
        }
        office += maph[flag][1];
        flag++;
    }
    return export_template(tpl, {
        charset: charset,
        type: type,
        table: office
    });
}
var doc = document;
var charset = doc.characterSet;

var uri = {
    /*json-wrap*/
    json: 'application/json;charset=' + charset,
    /*json-wrap*/
    /*txt-wrap*/
    txt: 'csv/txt;charset=' + charset,
    /*txt-wrap*/
    /*csv-wrap*/
    csv: 'csv/txt;charset=' + charset,
    /*csv-wrap*/
    /*xml-wrap*/
    xml: 'application/xml',
    /*xml-wrap*/
    /*doc-wrap*/
    doc: 'application/msword',
    /*doc-wrap*/
    /*xls-wrap*/
    xls: 'application/vnd.ms-excel',
    /*xls-wrap*/
    docx: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
};

function export_template(s, c) {
    return s.replace(/{{(\w+)}}/g, function (m, p) {
        return c[p];
    });
};

import {
    saveAs
} from "file-saver"

// 导出成excel文件， 参数： src, 带表头； rowKeys, 每一列key值按顺序排列； 生成 filename.type文件
var excel = function (src, rowKeys, filename, type) {
    var data = export_excel(src, rowKeys, charset, type);
    saveAs(new Blob([data], {
        type: uri[type]
    }), filename + '.' + type);
}

// excel([{"date":"2016-05-03","name":"王小虎_0","province":"上海","city":"普陀区","address":"上海市普陀区金沙江路 1518 弄","zip":20033},{"date":"2016-05-03","name":"王小虎_1","province":"上海","city":"普陀区","address":"上海市普陀区金沙江路 1518 弄","zip":20033},{"date":"2016-05-03","name":"王小虎_2","province":"上海","city":"普陀区","address":"上海市普陀区金沙江路 1518 弄","zip":20033},{"date":"2016-05-03","name":"王小虎_3","province":"上海","city":"普陀区","address":"上海市普陀区金沙江路 1518 弄","zip":20033},{"date":"2016-05-03","name":"王小虎_4","province":"上海","city":"普陀区","address":"上海市普陀区金沙江路 1518 弄","zip":20033}], [
//     "date",
//     "name",
//     "test",
//     "province",
//     "city",
//     "address",
//     "zip",
// ], "aaa", "xls")


function paramParse(key) {
    if (!location.search) return
    var paramArr = location.search.slice(1).split('&')
    var paramPair = {}
    for (var i = 0, len = paramArr.length; i < len; i++) {
        var item = paramArr[i];
        var param = item.split('=')
        paramPair[param[0]] = param[1]
    }
    if (key) return paramPair[key]
    return paramPair
}

function paramParseObj(key) {
    const value = paramParse(key)
    const decodeValue = decodeURIComponent(value)
    if (value && decodeValue) {
        return JSON.parse(decodeValue)
    }
}

function json2url(json) {
    var arr = []
    for (var i in json) {

        arr.push(i + '=' + (json[i].Format == undefined ? json[i] : json[i].Format("yy-MM-dd hh:mm:ss")))
    }
    return arr.join('&')
}

Date.prototype.Format = function (fmt) {
    // author: meizz
    var o = {
        "M+": this.getMonth() + 1, //月份
        "d+": this.getDate(), //日
        "h+": this.getHours(), //小时
        "m+": this.getMinutes(), //分
        "s+": this.getSeconds(), //秒
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度
        "S": this.getMilliseconds() //毫秒
    };
    if (/(y+)/.test(fmt))
        fmt = fmt.replace(RegExp.$1,
            (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt))
            fmt = fmt.replace(RegExp.$1,
                (RegExp.$1.length == 1) ?
                (o[k]) :
                (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}



export {
    addEvent,
    echo,
    excel,
    json2url,
    paramParseObj,
    paramParse,
    Vue,
}