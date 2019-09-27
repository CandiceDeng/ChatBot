$(function(){
  var template = Handlebars.compile(
    `
    <li class="clearfix">
        <div class="message-data align-right">
            <span class="message-data-time" >{{time}}, Today</span> &nbsp; &nbsp;
            <span class="message-data-name" >You</span> <i class="fa fa-circle me"></i>
        </div>
        <div class="message other-message float-right">
            {{messageOutput}}
        </div>
        </li>
    `
  );
  var templateResponse = Handlebars.compile(
    `
    <li>
    <div class="message-data">
        <span class="message-data-name"><i class="fa fa-circle online"></i> Candice</span>
        <span class="message-data-time">{{time}}, Today</span>
    </div>
    <div class="message my-message">
        {{response}}
    </div>
    </li>
    `
  )

    var chat = {
      messageToSend: '',
      init: function() {
        this.cacheDOM();
        this.bindEvents();
        this.render();
      },
      cacheDOM: function() {
        this.$chatHistory = $('.chat-history');
        this.$button = $('button');
        this.$textarea = $('#message-to-send');
        this.$chatHistoryList =  this.$chatHistory.find('ul');
      },
      bindEvents: function() {
        this.$button.on('click', this.addMessage.bind(this));
        this.$textarea.on('keyup', this.addMessageEnter.bind(this));
      },
      render: function() {
        this.scrollToBottom();
        if (this.messageToSend.trim() !== '') {
          var context = { 
            messageOutput: this.messageToSend,
            time: this.getCurrentTime()
          };
  
          this.$chatHistoryList.append(template(context));
          this.scrollToBottom();
          this.$textarea.val('');
          $.ajax({
            method: 'post',
            url: '/api/chatterbot',
            data: {
              csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val(),
              userInput: this.messageToSend.trim()
            }
            
          }).then((data) => {
            // responses
               
            var contextResponse = { 
              response: data.text,
              time: this.getCurrentTime()
            };
            this.$chatHistoryList.append(templateResponse(contextResponse));
            this.scrollToBottom();         
          })
           
  
        }
        
      },
      
      addMessage: function() {
        this.messageToSend = this.$textarea.val()
        this.render()
      },
      addMessageEnter: function(event) {
          // enter was pressed
          if (event.keyCode === 13) {
            this.addMessage();
          }
      },
      scrollToBottom: function() {
         this.$chatHistory.scrollTop(this.$chatHistory[0].scrollHeight);
      },
      getCurrentTime: function() {
        return new Date().toLocaleTimeString().
                replace(/([\d]+:[\d]{2})(:[\d]{2})(.*)/, "$1$3");
      },
      getRandomItem: function(arr) {
        return arr[Math.floor(Math.random()*arr.length)];
      }
      
    };
    
    chat.init();
    
    var searchFilter = {
      options: { valueNames: ['name'] },
      init: function() {
        var userList = new List('people-list', this.options);
        var noItems = $('<li id="no-items-found">No items found</li>');
        
        userList.on('updated', function(list) {
          if (list.matchingItems.length === 0) {
            $(list.list).append(noItems);
          } else {
            noItems.detach();
          }
        });
      }
    };
    
    searchFilter.init();
    
  });
  