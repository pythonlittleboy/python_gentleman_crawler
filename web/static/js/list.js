var app = new Vue({
  el: '#app',
  data: {
    items: []
  },
  methods: {
    addItems: function (items) {
      this.items.push.apply(this.items, items)
    },
    pickMovie: function(av_number) {
        var index = this.indexOfNumber(av_number);
        var item = this.items[index]
        this.items.splice(index,1)
        console.log(item.actor, item.av_number);
        var self = this;
        $.ajax({
            url: "/api/pick/" + item.actor + "/" + item.av_number,
            dataType: "text",
            success: function(result) {
                console.log("pick " + result)
                self.$message('下载成功: ' + item.actor + " " + item.av_number);
            }
        })
    },
    skipMovie: function(av_number) {
        var index = this.indexOfNumber(av_number);
        var item = this.items[index]
        console.log(item.actor, item.av_number)
        this.items.splice(index,1)
        var self = this;
        $.ajax({
            url: "/api/skip/" + item.av_number,
            dataType: "text",
            success: function() {
                self.$message('删除成功: ' + item.actor + " " + item.av_number);
            }
        })
    },

    indexOfNumber: function(av_number) {
        for (var i=0; i < this.items.length; i++) {
            if (av_number == this.items[i].av_number) {
                return i;
            }
        }
    }
  }
})

$(document).ready(function() {
    $.ajax({
        url: "/api/" + functionPath,
        dataType: "json",
        success: function(results) {
            // console.log(results)
            for (var i=0; i<results.length; i++) {
                var item = results[i];
                item.src = "/static/images/" + item.actor + "/" + item.av_number + ".jpg";
                item.new_title = item.av_number + " " + item.title;
                item.index = i;
            }

            app.addItems(results)
        }
    })
})
