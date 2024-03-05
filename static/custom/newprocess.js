$(document).ready(function () {
	initFileUploader('#zdrop');
	function initFileUploader(target) {
		var previewNode = document.querySelector('#zdrop-template');
		previewNode.id = '';
		var previewTemplate = previewNode.parentNode.innerHTML;
		previewNode.parentNode.removeChild(previewNode);

		var zdrop = new Dropzone(target, {
			url: '/new-file/',
			maxFiles: 5,
			maxFilesize: 500,
			previewTemplate: previewTemplate,
			previewsContainer: '#previews',
			clickable: '#upload-label',
			acceptedFiles:
				'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
		});

		zdrop.on('addedfile', function (file) {
			$('.preview-container').css('visibility', 'visible');
		});

		zdrop.on('totaluploadprogress', function (progress) {
			var progr = document.querySelector('.progress .determinate');
			if (progr === undefined || progr === null) return;

			progr.style.width = progress + '%';
		});

		zdrop.on('dragenter', function () {
			$('.fileuploader').addClass('active');
		});

		zdrop.on('dragleave', function () {
			$('.fileuploader').removeClass('active');
		});

		zdrop.on('drop', function () {
			$('.fileuploader').removeClass('active');
		});

		$('.Submit').click(async function (e) {
			e.preventDefault();
			let cs = $('input[name="csrfmiddlewaretoken"]').val();
			let files = zdrop.files;
			let fd = new FormData();
			fd.append('csrfmiddlewaretoken', cs);
			for (var x = 0; x < files.length; x++) {
				fd.append('files', files[x]);
			}
			$('.Loader').removeClass('d-none');
			let post = await fetch('/new-proccess/', {
				method: 'post',
				body: fd,
			});
			if (post.status == 200) {
				$('.Loader').addClass('d-none');
				Done('محصولات با موفقیت اضافه شدند!');
				setTimeout(() => window.location.reload(), 4000);
			} else {
				$('.Loader').addClass('d-none');
				Failed('مشکلی پیش آمده است!');
			}
		});
	}
});
