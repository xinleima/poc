$(document).ready(function () {
  $('.tab-group li.tab-control').on('click', function () {
    var activeLi = $('.tab-group li.tab-control.active');
    $(activeLi.attr('data-target')).hide();
    activeLi.removeClass("active");

    $($(this).attr('data-target')).show();
    $(this).addClass("active");
  });

  $('.toggle-group li').on('click', function () {
    console.log("in click");
    var activeLi = $('.toggle-group li.active');
    if(activeLi!==$(this)){
      activeLi.removeClass("active");
      $(this).addClass("active");
    }
    $($(this).attr('data-target')).slideToggle(500);
  });

  $('#login-form').submit(function (event) {
    event.preventDefault();
    var actionUrl = $(this)[0].action;
    var username = $(this)[0].username.value;
    var password =  $(this)[0].password.value;
    $.post(actionUrl,
      {username:username,password:password},
      function (data) {
        var jsonData = JSON.parse(data);
        if(jsonData.state === 0){
          window.location.href = "/project";
        }
        else{
          $('#login-msg-div').show();
        }
      }
    )
  });

  $('#register-form').submit(function (event) {
    event.preventDefault();
    var actionUrl = $(this)[0].action;
    var username = $(this)[0].username.value;
    var password =  $(this)[0].password.value;
    var repeatPassword = $(this)[0]['repeat-password'].value;

    if(repeatPassword !== password) {
      $('.password-div').addClass("has-error");
      $('#register-password-msg').show();
      return;
    }
    $.post(actionUrl,
      {
        username:username,
        password:password
      },
      function (data) {
        var jsonData = JSON.parse(data);
        if(jsonData.state === 0){
          $('#login-msg').text("注册成功，请登录！");
          $('#login-msg-div').removeClass("has-error").addClass("has-success").show();
          $('#login-li').click();
        }
        else{
          $('#login-msg').text("注册成功，请登录！");
          $('#login-msg-div').removeClass("has-error").addClass("has-success").show();
          $('#login-li').click();
        }
      }
    )
  });

  $('.data-list-a').on('click',function (event) {
    event.preventDefault();
    $.get($(this).attr('href'),function (data) {
      var dataListTable = $('#data-list-table');
      dataListTable.children().remove();
      var tbody = $('<tbody></tbody>');
      dataListTable.append(tbody);


      var jsonData = JSON.parse(data);

      var curTr = $("<tr></tr>");
      jsonData.fields.forEach(function (field) {
        curTr.append($("<th></th>").text(field));
      });
      tbody.append(curTr);

      jsonData.datas.forEach(function (fieldDatas) {
        curTr = $("<tr></tr>");
        fieldDatas.forEach(function (fieldData) {
          curTr.append($("<td></td>").text(fieldData));
        });
        tbody.append(curTr);
      });
    });
  });

});
