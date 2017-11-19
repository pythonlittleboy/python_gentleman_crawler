var start = 0, limit = 20;

var app = new Vue({
  el: '#app',
  data: {
    total: 5000,
    start: 0,
    limit: 40,
    currentPage: 1,
    items: []
  },
  mounted: function() {
     console.log("mounted")
     this.load();
  },
  methods: {
    addItems: function (items) {
      this.items = [];
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
    },

    handleCurrentChange: function(val) {
        this.start = this.limit * parseInt(val - 1);
        this.load();
    },

    load : function() {
        var self = this;

        if (functionPath == "search" && keyword && keyword != "") {
            url = functionPath + "/" + keyword
        } else {
            url = functionPath
        }

        $.ajax({
            url: "/api/" + url,
            data: {start: self.start, limit: self.limit},
            dataType: "json",
            success: function(result) {
                // console.log(results)
                var movies = result.movies;
                self.total = parseInt(result.total);

                for (var i=0; i<movies.length; i++) {
                    var item = movies[i];
                    //item.src = "/static/images/" + item.actor + "/" + item.av_number + ".jpg";
                    item.src = "/static/images/" + item.short_name + "/" + item.av_number + ".jpg";
                    item.new_title = item.av_number + " " + item.title;
                    item.index = i;
                }

                self.addItems(movies)
                document.body.scrollTop = 0;
            }
        })
    }
  }
})

/*
$(document).ready(function() {
    $.ajax({
        url: "/api/" + functionPath,
        data: {start: start, limit: limit},
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
*/