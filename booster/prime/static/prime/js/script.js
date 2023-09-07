
function validate_form ( )
{
	valid = true;

        if ( document.estimate_form.name.value == "" )
        {
                alert ( "Пожалуйста заполните поле 'Ваше имя'." );
                valid = false;
        }

        return valid;
}