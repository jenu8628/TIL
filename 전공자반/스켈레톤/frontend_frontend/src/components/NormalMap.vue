<template>
  <div>
    <div style="margin-bottom: 50px; backround-color: gray;">
      <b-form-checkbox-group
        id="checkbox-group-2"
        v-model="house_sel"
        name="flavour-2"
      >
        <b-form-checkbox size="lg" value="1">아파트</b-form-checkbox>
        <b-form-checkbox size="lg" value="2">빌라</b-form-checkbox>
        <b-form-checkbox size="lg" value="3">오피스텔</b-form-checkbox>
      </b-form-checkbox-group>
      <b-form-checkbox-group
        id="checkbox-group-2"
        v-model="school_sel"
        name="flavour-2"
      >
        <b-form-checkbox size="lg" value="초등학교">초등학교</b-form-checkbox>
        <b-form-checkbox size="lg" value="중학교">중학교</b-form-checkbox>
        <b-form-checkbox size="lg" value="고등학교">고등학교</b-form-checkbox>
      </b-form-checkbox-group>
      <b-form-checkbox v-model="corona_sel" value="1">
        코로나 진료소
      </b-form-checkbox>
      <b-form-checkbox v-model="cctv_sel" value="1">
        CCTV
      </b-form-checkbox>
    </div>
    <div id="map"></div>
  </div>
</template>

<script>
import axios from "@/plugins/axios";

export default {
  created() {},
  data() {
    return {
      map: null,
      house: [],
      house_marker: [],
      house_custom: [],
      house_sel: [1, 2, 3],
      school: [],
      school_marker: [],
      school_sel: [],
      school_custom: [],
      corona_sel: "",
      corona: [],
      corona_marker: [],
      corona_custom: [],
      cctv_sel: "",
      cctv: [],
      cctv_marker: [],
      bus: []
    };
  },
  watch: {
    corona_sel: {
      handler: function() {
        // 인포윈도우를 표시하는 클로저를 만드는 함수입니다
        function CoronaMakeOverListener(map, CustomOverlay) {
          return function() {
            CustomOverlay.setMap(map);
          };
        }

        // 인포윈도우를 닫는 클로저를 만드는 함수입니다
        function CoronaMakeOutListener(CustomOverlay) {
          return function() {
            CustomOverlay.setMap(null);
          };
        }

        var t = this.corona_marker.length;
        for (var i = 0; i < t; i++) {
          this.corona_marker[i].setMap(null);
        }
        t = this.corona_custom.length;
        for (i = 0; i < t; i++) {
          this.corona_custom[i].setMap(null);
        }

        var markerImage = new kakao.maps.MarkerImage(
          require("@/assets/corona_icon.png"),
          new kakao.maps.Size(52, 75)
        );

        t = this.corona.length;
        for (i = 0; i < t; i++) {
          if (this.corona_sel != "1") {
            break;
          }
          // 마커생성
          var marker = new kakao.maps.Marker({
            map: this.map,
            position: new kakao.maps.LatLng(
              this.corona[i]["clinic_lat"],
              this.corona[i]["clinic_lng"]
            ),
            image: markerImage,
            clickable: true
          });
          this.corona_marker.push(marker);

          // 마커에 표시할 인포우
          var content =
            '<div class="overlay_info">' +
            '<div class="card" style="width:250px; heigh="200px;">' +
            '<div class="card-body">' +
            '<h5 class="card-title">' +
            this.corona[i]["clinic_name"] +
            "</h5>" +
            "<hr />" +
            '<p class="card-text">' +
            this.corona[i]["phone_number"] +
            "</p>" +
            "<hr />" +
            '<p class="card-text"> 평일 : ' +
            this.corona[i]["weekday_time"] +
            "</p>" +
            "<hr />" +
            '<p class="card-text"> 토요일 : ' +
            this.corona[i]["saturday_time"] +
            "</p>" +
            "<hr />" +
            '<p class="card-text"> 일요일 : ' +
            this.corona[i]["sunday_time"] +
            "</p>" +
            "</div>" +
            "</div>" +
            "</div>";

          let level = this.map.getLevel();
          let add;
          if (level == 1) add = 0.0005;
          else if (level == 2) add = 0.001;
          else if (level == 3) add = 0.002;
          else if (level == 4) add = 0.004;
          else if (level == 5) add = 0.008;
          else if (level == 6) add = 0.016;
          else if (level == 7) add = 0.032;

          var custom = new kakao.maps.CustomOverlay({
            content: content,
            position: new kakao.maps.LatLng(
              Number(this.corona[i]["clinic_lat"]) + add,
              Number(this.corona[i]["clinic_lng"])
            )
          });
          this.corona_custom.push(custom);

          //마커 리스너
          kakao.maps.event.addListener(
            marker,
            "mouseover",
            CoronaMakeOverListener(this.map, custom)
          );
          kakao.maps.event.addListener(
            marker,
            "mouseout",
            CoronaMakeOutListener(custom)
          );
        }
      }
    },
    cctv_sel: {
      handler: function() {
        var t = this.cctv_marker.length;
        for (i = 0; i < t; i++) {
          this.cctv_marker[i].setMap(null);
        }

        var markerImage = new kakao.maps.MarkerImage(
          require("@/assets/cctv_icon.png"),
          new kakao.maps.Size(20, 40)
        );

        t = this.cctv.length;
        for (var i = 0; i < t; i++) {
          if (this.cctv_sel != "1") {
            return;
          }
          // 마커생성
          var marker = new kakao.maps.Marker({
            map: this.map,
            position: new kakao.maps.LatLng(
              this.cctv[i]["lat"],
              this.cctv[i]["lng"]
            ),
            image: markerImage,
            clickable: true
          });
          this.cctv_marker.push(marker);
        }
      }
    },
    school_sel: {
      handler: function() {
        // 인포윈도우를 표시하는 클로저를 만드는 함수입니다
        function SchoolMakeOverListener(map, CustomOverlay) {
          return function() {
            CustomOverlay.setMap(map);
          };
        }

        // 인포윈도우를 닫는 클로저를 만드는 함수입니다
        function SchoolMakeOutListener(CustomOverlay) {
          return function() {
            CustomOverlay.setMap(null);
          };
        }

        t = this.school_marker.length;
        for (var i = 0; i < t; i++) {
          this.school_marker[i].setMap(null);
        }
        t = this.school_marker.length;
        for (i = 0; i < t; i++) {
          this.school_custom[i].setMap(null);
        }

        var ssl = this.school_sel.length;

        var markerImage = new kakao.maps.MarkerImage(
          require("@/assets/school_icon.png"),
          new kakao.maps.Size(60, 75)
        );

        var t = this.school.length;
        for (i = 0; i < t; i++) {
          for (let h = 0; h < ssl; h++) {
            if (this.school_sel[h] != this.school[i]["school_grade"]) {
              continue;
            }
            // 마커생성
            var marker = new kakao.maps.Marker({
              map: this.map,
              position: new kakao.maps.LatLng(
                this.school[i]["lat"],
                this.school[i]["lng"]
              ),
              image: markerImage,
              clickable: true
            });
            this.school_marker.push(marker);

            // 마커에 표시할 인포우
            var content =
              '<div class="overlay_info">' +
              '<div class="card" style="width:250px; heigh="200px;">' +
              this.school[i]["school_name"] +
              "</div>" +
              "</div>";

            let level = this.map.getLevel();
            let add;
            if (level == 1) add = 0.0006;
            else if (level == 2) add = 0.0001;
            else if (level == 3) add = 0.0003;
            else if (level == 4) add = 0.0014;
            else if (level == 5) add = 0.0028;
            else if (level == 6) add = 0.0056;
            else if (level == 7) add = 0.01;

            var custom = new kakao.maps.CustomOverlay({
              content: content,
              position: new kakao.maps.LatLng(
                Number(this.school[i]["lat"]) + add,
                Number(this.school[i]["lng"])
              )
            });
            this.school_custom.push(custom);

            //마커 리스너
            kakao.maps.event.addListener(
              marker,
              "mouseover",
              SchoolMakeOverListener(this.map, custom)
            );
            kakao.maps.event.addListener(
              marker,
              "mouseout",
              SchoolMakeOutListener(custom)
            );
          }
        }
      }
    },
    house_sel: {
      handler: function() {
        // 인포윈도우를 표시하는 클로저를 만드는 함수입니다
        function makeOverListener(map, CustomOverlay) {
          return function() {
            CustomOverlay.setMap(map);
          };
        }

        // 인포윈도우를 닫는 클로저를 만드는 함수입니다
        function makeOutListener(CustomOverlay) {
          return function() {
            CustomOverlay.setMap(null);
          };
        }
        var t = this.house_marker.length;
        for (var i = 0; i < t; i++) {
          this.house_marker[i].setMap(null);
        }
        t = this.house_custom.length;
        for (i = 0; i < t; i++) {
          this.house_custom[i].setMap(null);
        }

        var hsl = this.house_sel.length;

        var markerImage = new kakao.maps.MarkerImage(
          require("@/assets/house_icon.png"),
          new kakao.maps.Size(52, 75)
        );

        t = this.house.length;
        for (i = 0; i < t; i++) {
          for (let h = 0; h < hsl; h++) {
            if (this.house_sel[h] != this.house[i]["type"]) {
              continue;
            }
            // 마커생성
            var marker = new kakao.maps.Marker({
              map: this.map,
              position: new kakao.maps.LatLng(
                this.house[i]["house_lat"],
                this.house[i]["house_lng"]
              ),
              image: markerImage,
              clickable: true
            });
            this.house_marker.push(marker);

            // 마커에 표시할 인포우
            var content =
              '<div class="overlay_info">' +
              '<div class="card" style="width:250px; heigh="200px;">' +
              '<img class="card-img-top" src="https://pds.joins.com/news/component/htmlphoto_mmdata/201809/14/8f85c1c7-7e6c-438a-92ba-24ae1e57615e.jpg" alt="Card image" heigh="90%" widh="90%">' +
              '<div class="card-body">' +
              '<h5 class="card-title">' +
              this.house[i]["house_name"] +
              "</h5>" +
              "<hr />" +
              '<p class="card-text">' +
              this.house[i]["deal_amount"] +
              "만원</p>" +
              "<hr />" +
              '<p class="card-text">' +
              this.house[i]["area"] +
              "평</p>" +
              "<hr />" +
              '<p class="card-text">' +
              this.house[i]["floor"] +
              "층</p>" +
              "</div>" +
              "</div>" +
              "</div>";
            let level = this.map.getLevel();
            let add;
            if (level == 1) add = 0.0006;
            else if (level == 2) add = 0.0012;
            else if (level == 3) add = 0.0024;
            else if (level == 4) add = 0.0048;
            else if (level == 5) add = 0.0096;
            else if (level == 6) add = 0.0192;
            else if (level == 7) add = 0.038;

            var custom = new kakao.maps.CustomOverlay({
              content: content,
              position: new kakao.maps.LatLng(
                Number(this.house[i]["house_lat"]) + add,
                Number(this.house[i]["house_lng"])
              )
            });
            this.house_custom.push(custom);

            //마커 리스너
            kakao.maps.event.addListener(
              marker,
              "mouseover",
              makeOverListener(this.map, custom)
            );
            kakao.maps.event.addListener(
              marker,
              "mouseout",
              makeOutListener(custom)
            );
          }
        }
      },
      deep: true
    }
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
    } else {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=184dc5169bac041d61de0e59b6e4b6ed&libraries=services,clusterer,drawing";
      document.head.appendChild(script);
    }
  },
  methods: {
    initMap() {
      var container = document.getElementById("map");
      var options = {
        center: new kakao.maps.LatLng(37.5666805, 126.9784147),
        level: 4
      };

      var tmap = new kakao.maps.Map(container, options);

      // 지도 타입 변경 컨트롤을 생성한다
      var mapTypeControl = new kakao.maps.MapTypeControl();

      // 지도의 상단 우측에 지도 타입 변경 컨트롤을 추가한다
      tmap.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

      // 지도에 확대 축소 컨트롤을 생성한다
      var zoomControl = new kakao.maps.ZoomControl();

      // 지도의 우측에 확대 축소 컨트롤을 추가한다
      tmap.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

      this.map = tmap;

      var start = tmap => {
        // 지도 영역정보를 얻어옵니다
        var bounds = tmap.getBounds();

        // 영역정보의 남서쪽 정보를 얻어옵니다
        var swLatlng = bounds.getSouthWest();

        // 영역정보의 북동쪽 정보를 얻어옵니다
        var neLatlng = bounds.getNorthEast();

        axios({
          method: "post",
          url: "/api/house/latlng",
          data: {
            minlat: swLatlng["Ma"],
            minlng: swLatlng["La"],
            maxlat: neLatlng["Ma"],
            maxlng: neLatlng["La"]
          }
        }).then(response => {
          this.house = response.data["house"];
          this.cctv = response.data["cctv"];
          this.corona = response.data["corona"];
          this.school = response.data["school"];

          //////////////////////////////////
          //// HOUSE
          //////////////////////////////////

          // 인포윈도우를 표시하는 클로저를 만드는 함수입니다
          function MakeOverListener(map, CustomOverlay) {
            return function() {
              CustomOverlay.setMap(map);
            };
          }

          // 인포윈도우를 닫는 클로저를 만드는 함수입니다
          function MakeOutListener(CustomOverlay) {
            return function() {
              CustomOverlay.setMap(null);
            };
          }

          var t = this.house_marker.length;
          for (var i = 0; i < t; i++) {
            this.house_marker[i].setMap(null);
          }
          t = this.house_custom.length;
          for (i = 0; i < t; i++) {
            this.house_custom[i].setMap(null);
          }

          var hsl = this.house_sel.length;

          var markerImage = new kakao.maps.MarkerImage(
            require("@/assets/house_icon.png"),
            new kakao.maps.Size(52, 75)
          );

          t = this.house.length;
          for (i = 0; i < t; i++) {
            for (let h = 0; h < hsl; h++) {
              if (this.house_sel[h] != this.house[i]["type"]) {
                continue;
              }
              // 마커생성
              var marker = new kakao.maps.Marker({
                map: this.map,
                position: new kakao.maps.LatLng(
                  this.house[i]["house_lat"],
                  this.house[i]["house_lng"]
                ),
                image: markerImage,
                clickable: true
              });
              this.house_marker.push(marker);

              // 마커에 표시할 인포우
              var content =
                '<div class="overlay_info">' +
                '<div class="card" style="width:250px; heigh="200px;">' +
                '<img class="card-img-top" src="https://pds.joins.com/news/component/htmlphoto_mmdata/201809/14/8f85c1c7-7e6c-438a-92ba-24ae1e57615e.jpg" alt="Card image" heigh="90%" widh="90%">' +
                '<div class="card-body">' +
                '<h5 class="card-title">' +
                this.house[i]["house_name"] +
                "</h5>" +
                "<hr />" +
                '<p class="card-text">' +
                this.house[i]["deal_amount"] +
                "만원</p>" +
                "<hr />" +
                '<p class="card-text">' +
                this.house[i]["area"] +
                "평</p>" +
                "<hr />" +
                '<p class="card-text">' +
                this.house[i]["floor"] +
                "층</p>" +
                "</div>" +
                "</div>" +
                "</div>";

              let level = this.map.getLevel();
              let add;
              if (level == 1) add = 0.0006;
              else if (level == 2) add = 0.0012;
              else if (level == 3) add = 0.0024;
              else if (level == 4) add = 0.0048;
              else if (level == 5) add = 0.0096;
              else if (level == 6) add = 0.0192;
              else if (level == 7) add = 0.038;

              var custom = new kakao.maps.CustomOverlay({
                content: content,
                position: new kakao.maps.LatLng(
                  Number(this.house[i]["house_lat"]) + add,
                  Number(this.house[i]["house_lng"])
                )
              });
              this.house_custom.push(custom);

              //마커 리스너
              kakao.maps.event.addListener(
                marker,
                "mouseover",
                MakeOverListener(this.map, custom)
              );
              kakao.maps.event.addListener(
                marker,
                "mouseout",
                MakeOutListener(custom)
              );
            }
          }

          //////////////////////////////////
          //// SCHOOL
          /////////////////////////////////

          // 인포윈도우를 표시하는 클로저를 만드는 함수입니다
          function SchoolMakeOverListener(map, CustomOverlay) {
            return function() {
              CustomOverlay.setMap(map);
            };
          }

          // 인포윈도우를 닫는 클로저를 만드는 함수입니다
          function SchoolMakeOutListener(CustomOverlay) {
            return function() {
              CustomOverlay.setMap(null);
            };
          }

          t = this.school_marker.length;
          for (i = 0; i < t; i++) {
            this.school_marker[i].setMap(null);
          }
          t = this.school_marker.length;
          for (i = 0; i < t; i++) {
            this.school_custom[i].setMap(null);
          }

          var ssl = this.school_sel.length;

          markerImage = new kakao.maps.MarkerImage(
            require("@/assets/school_icon.png"),
            new kakao.maps.Size(60, 75)
          );

          t = this.school.length;
          for (i = 0; i < t; i++) {
            for (let h = 0; h < ssl; h++) {
              if (this.school_sel[h] != this.school[i]["school_grade"]) {
                continue;
              }
              // 마커생성
              marker = new kakao.maps.Marker({
                map: this.map,
                position: new kakao.maps.LatLng(
                  this.school[i]["lat"],
                  this.school[i]["lng"]
                ),
                image: markerImage,
                clickable: true
              });
              this.school_marker.push(marker);

              // 마커에 표시할 인포우
              content =
                '<div class="overlay_info">' +
                '<div class="card" style="width:250px; heigh="200px;">' +
                this.school[i]["school_name"] +
                "</div>" +
                "</div>";

              let level = this.map.getLevel();
              let add;
              if (level == 1) add = 0.0006;
              else if (level == 2) add = 0.0001;
              else if (level == 3) add = 0.0003;
              else if (level == 4) add = 0.0014;
              else if (level == 5) add = 0.0028;
              else if (level == 6) add = 0.0056;
              else if (level == 7) add = 0.01;

              custom = new kakao.maps.CustomOverlay({
                content: content,
                position: new kakao.maps.LatLng(
                  Number(this.school[i]["lat"]) + add,
                  Number(this.school[i]["lng"])
                )
              });
              this.school_custom.push(custom);

              //마커 리스너
              kakao.maps.event.addListener(
                marker,
                "mouseover",
                SchoolMakeOverListener(this.map, custom)
              );
              kakao.maps.event.addListener(
                marker,
                "mouseout",
                SchoolMakeOutListener(custom)
              );
            }
          }

          ///////////////////////////////////
          //// CCTV
          //////////////////////////////////
          t = this.cctv_marker.length;
          for (i = 0; i < t; i++) {
            this.cctv_marker[i].setMap(null);
          }

          markerImage = new kakao.maps.MarkerImage(
            require("@/assets/cctv_icon.png"),
            new kakao.maps.Size(20, 40)
          );

          t = this.cctv.length;
          for (i = 0; i < t; i++) {
            if (this.cctv_sel != "1") {
              break;
            }
            // 마커생성
            marker = new kakao.maps.Marker({
              map: this.map,
              position: new kakao.maps.LatLng(
                this.cctv[i]["lat"],
                this.cctv[i]["lng"]
              ),
              image: markerImage,
              clickable: true
            });
            this.cctv_marker.push(marker);
          }

          //////////////////////////////////
          //// CORONA
          //////////////////////////////////

          // 인포윈도우를 표시하는 클로저를 만드는 함수입니다
          function CoronaMakeOverListener(map, CustomOverlay) {
            return function() {
              CustomOverlay.setMap(map);
            };
          }

          // 인포윈도우를 닫는 클로저를 만드는 함수입니다
          function CoronaMakeOutListener(CustomOverlay) {
            return function() {
              CustomOverlay.setMap(null);
            };
          }

          t = this.corona_marker.length;
          for (i = 0; i < t; i++) {
            this.corona_marker[i].setMap(null);
          }
          t = this.corona_custom.length;
          for (i = 0; i < t; i++) {
            this.corona_custom[i].setMap(null);
          }

          markerImage = new kakao.maps.MarkerImage(
            require("@/assets/corona_icon.png"),
            new kakao.maps.Size(52, 75)
          );

          t = this.corona.length;
          for (i = 0; i < t; i++) {
            if (this.corona_sel != "1") {
              break;
            }
            // 마커생성
            marker = new kakao.maps.Marker({
              map: this.map,
              position: new kakao.maps.LatLng(
                this.corona[i]["clinic_lat"],
                this.corona[i]["clinic_lng"]
              ),
              image: markerImage,
              clickable: true
            });
            this.corona_marker.push(marker);

            // 마커에 표시할 인포우
            content =
              '<div class="overlay_info">' +
              '<div class="card" style="width:250px; heigh="200px;">' +
              '<div class="card-body">' +
              '<h5 class="card-title">' +
              this.corona[i]["clinic_name"] +
              "</h5>" +
              "<hr />" +
              '<p class="card-text">' +
              this.corona[i]["phone_number"] +
              "</p>" +
              "<hr />" +
              '<p class="card-text"> 평일 : ' +
              this.corona[i]["weekday_time"] +
              "</p>" +
              "<hr />" +
              '<p class="card-text"> 토요일 : ' +
              this.corona[i]["saturday_time"] +
              "</p>" +
              "<hr />" +
              '<p class="card-text"> 일요일 : ' +
              this.corona[i]["sunday_time"] +
              "</p>" +
              "</div>" +
              "</div>" +
              "</div>";

            let level = this.map.getLevel();
            let add;
            if (level == 1) add = 0.0005;
            else if (level == 2) add = 0.001;
            else if (level == 3) add = 0.002;
            else if (level == 4) add = 0.004;
            else if (level == 5) add = 0.008;
            else if (level == 6) add = 0.016;
            else if (level == 7) add = 0.032;

            custom = new kakao.maps.CustomOverlay({
              content: content,
              position: new kakao.maps.LatLng(
                Number(this.corona[i]["clinic_lat"]) + add,
                Number(this.corona[i]["clinic_lng"])
              )
            });
            this.corona_custom.push(custom);

            //마커 리스너
            kakao.maps.event.addListener(
              marker,
              "mouseover",
              CoronaMakeOverListener(this.map, custom)
            );
            kakao.maps.event.addListener(
              marker,
              "mouseout",
              CoronaMakeOutListener(custom)
            );
          }
        }); // axios end
      }; // start() end

      kakao.maps.event.addListener(tmap, "zoom_changed", function() {
        start(tmap);
      });

      kakao.maps.event.addListener(tmap, "dragend", function() {
        start(tmap);
      });

      axios.defaults.headers.common["Authorization"] = JSON.parse(
        localStorage.getItem("vuex")
      )["token"]["acc_token"];
      start(tmap);
    }
  }
};
</script>

<style>
#map {
  margin-left: auto;
  margin-right: auto;
  width: 80%;
  height: 850px;
}
</style>
