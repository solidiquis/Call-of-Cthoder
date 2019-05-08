//Displays the comment-reply-form
$(document).ready(function(){

	$('.reply-secondary').click(function(e){
		var this_ = $(this);
		var replyID = this_.attr('reply-id')
		var allForms = $('.reply-secondary-form');
		var allEditForms = $('.edit-reply-secondary-form');

		//Closes all other open comment-reply-forms and edit forms
		for (let form of allForms){
			form.style.display = 'none'
		};

		for (let form of allEditForms){
			form.style.display = 'none'
		};

		$(`.reply-secondary-form[reply-id="${replyID}"]`).css('display', 'flex')
	})
});

//Logic for the cancel button which closes comment-reply-form.
$(document).ready(function(){
	$('.cancel-reply-secondary').click(function(e){
		var this_ = $(this);
		var replyID = this_.attr('reply-id');
		$(`.reply-secondary-form[reply-id="${replyID}"]`).css('display', 'none');
	})
});

$(document).ready(function(){
	$('.reply-secondary-form').submit(function(e){
		e.preventDefault();
		var this_ = $(this);
		var urlEndpoint = this_.attr('action');
		var parentCommentID = this_.attr('parent-comment-id');
		var formData = this_.serialize();

		$.ajax({
			url: urlEndpoint,
			method: 'POST',
			data: formData,
			success: function(response){
				$(`.replies[comment-id="${parentCommentID}"]`).html(response['replies']);
				this_.css('display', 'none');
				$("textarea[name='reply_body']").val('');
			},
		})
	})
})
