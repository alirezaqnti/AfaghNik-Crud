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
				Done('Datas Added Succesfully');
				setTimeout(() => $('#crud-tab').trigger('click'), 1000);
			} else {
				$('.Loader').addClass('d-none');
				Failed("There's been a Problem");
			}
		});
	}
});

$('#crud-tab').click(async function () {
	let getData = await fetch('/dataset/');
	let datas = await getData.json();
	$('#Passengers').empty();
	datas.forEach((x) => {
		$('#Passengers').append(`
	  <option value="${x.id}"
		data-PassengerId="${x.PassengerId}"
		data-Survived="${x.Survived}"
		data-Pclass="${x.Pclass}"
		data-Name="${x.Name}"
		data-Sex="${x.Sex}"
		data-Age="${x.Age}"
		data-SibSp="${x.SibSp}"
		data-Parch="${x.Parch}"
		data-Ticket="${x.Ticket}"
		data-Fare="${x.Fare}"
		data-Cabin="${x.Cabin}"
		data-Embarked="${x.Embarked}"
		>
		${x.Name}
	  </option>
	  `);
	});
	$('#Passengers').children('option').first().attr('selected', true);
	$('#Passengers').trigger('change');
});
$('#Passengers').change(function () {
	let val = $(this).val()[0];
	let option = $(`#Passengers option[value='${val}']`);
	$('#Survived').val($(option).data('survived'));
	$('#Pclass').val($(option).data('pclass'));
	$('#Name').val($(option).data('name'));
	$('#Sex').val($(option).data('sex'));
	$('#Age').val($(option).data('age'));
	$('#SibSp').val($(option).data('sibsp'));
	$('#Parch').val($(option).data('parch'));
	$('#Ticket').val($(option).data('ticket'));
	$('#Fare').val($(option).data('fare'));
	$('#Cabin').val($(option).data('cabin'));
	$('#Embarked').val($(option).data('embarked'));
});
$('.update-btn').click(async function (e) {
	e.preventDefault();
	let val = $('#Passengers').val();
	let Survived = $(`#UpdateForm input[name='Survived']`).val();
	let Pclass = $(`#UpdateForm input[name='Pclass']`).val();
	let Name = $(`#UpdateForm input[name='Name']`).val();
	let Sex = $(`#UpdateForm input[name='Sex']`).val();
	let Age = $(`#UpdateForm input[name='Age']`).val();
	let SibSp = $(`#UpdateForm input[name='SibSp']`).val();
	let Parch = $(`#UpdateForm input[name='Parch']`).val();
	let Ticket = $(`#UpdateForm input[name='Ticket']`).val();
	let Fare = $(`#UpdateForm input[name='Fare']`).val();
	let Cabin = $(`#UpdateForm input[name='Cabin']`).val();
	let Embarked = $(`#UpdateForm input[name='Embarked']`).val();
	const myHeaders = new Headers();
	myHeaders.append('Content-Type', 'application/json');
	myHeaders.append(
		'X-CSRFToken',
		$('#UpdateForm input[name="csrfmiddlewaretoken"]').val()
	);

	let put = await fetch(`/dataset/${val[0]}/`, {
		method: 'PUT',
		headers: myHeaders,
		redirect: 'follow',
		body: JSON.stringify({
			id: val[0],
			Survived: Survived,
			Pclass: Pclass,
			Name: Name,
			Sex: Sex,
			Age: Age,
			SibSp: SibSp,
			Parch: Parch,
			Ticket: Ticket,
			Fare: Fare,
			Cabin: Cabin,
			Embarked: Embarked,
		}),
	});
	console.log('PUT:', put.status);
	if (put.status == 200) {
		Done('Updated!');
		$('#crud-tab').trigger('click');
	}
});

$('.destroy-btn').click(async function (e) {
	e.preventDefault();
	let val = $('#Passengers').val();
	const myHeaders = new Headers();
	myHeaders.append('Content-Type', 'multipart/form-data');
	myHeaders.append(
		'X-CSRFToken',
		$('#UpdateForm input[name="csrfmiddlewaretoken"]').val()
	);
	let del = await fetch(`/dataset/${val}/`, {
		method: 'DELETE',
		headers: myHeaders,
		redirect: 'follow',
	});
	if (del.status == 204) {
		Done('Deleted!');
		$('#crud-tab').trigger('click');
	}
});
$('.newPassenger').click(function (e) {
	$('.newPassenger').addClass('d-none');
	$('.newPassenger').fadeOut();
	$('.EditPassengers').removeClass('d-none');
	$('.EditPassengers').fadeIn();
	$('.data-form').fadeOut();
	$('.data-form').addClass('d-none');
	$('.data-new-form').removeClass('d-none');
	$('.data-new-form').fadeIn();
});
$('.EditPassengers').click(function (e) {
	$('.EditPassengers').addClass('d-none');
	$('.EditPassengers').fadeOut();
	$('.newPassenger').removeClass('d-none');
	$('.newPassenger').fadeIn();
	$('.data-new-form').fadeOut();
	$('.data-new-form').addClass('d-none');
	$('.data-form').removeClass('d-none');
	$('.data-form').fadeIn();
});
$('.submit-btn').click(async function (e) {
	e.preventDefault();
	let val = $('#Passengers').val();
	let Survived = $(`#NewForm input[name='Survived']`).val();
	let Pclass = $(`#NewForm input[name='Pclass']`).val();
	let Name = $(`#NewForm input[name='Name']`).val();
	let Sex = $(`#NewForm input[name='Sex']`).val();
	let Age = $(`#NewForm input[name='Age']`).val();
	let SibSp = $(`#NewForm input[name='SibSp']`).val();
	let Parch = $(`#NewForm input[name='Parch']`).val();
	let Ticket = $(`#NewForm input[name='Ticket']`).val();
	let Fare = $(`#NewForm input[name='Fare']`).val();
	let Cabin = $(`#NewForm input[name='Cabin']`).val();
	let Embarked = $(`#NewForm input[name='Embarked']`).val();
	const myHeaders = new Headers();
	myHeaders.append('Content-Type', 'application/json');
	myHeaders.append(
		'X-CSRFToken',
		$('#NewForm input[name="csrfmiddlewaretoken"]').val()
	);
	let post = await fetch(`/dataset/`, {
		method: 'POST',
		headers: myHeaders,
		redirect: 'follow',
		body: JSON.stringify({
			Survived: Survived,
			Pclass: Pclass,
			Name: Name,
			Sex: Sex,
			Age: Age,
			SibSp: SibSp,
			Parch: Parch,
			Ticket: Ticket,
			Fare: Fare,
			Cabin: Cabin,
			Embarked: Embarked,
		}),
	});
	console.log('POST:', post.status);
	if (post.status == 201) {
		Done('Submited!');
		$('#crud-tab').trigger('click');
		$('.EditPassengers').trigger('click');
	}
});
