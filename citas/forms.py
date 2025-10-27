# citas/forms.py
from django import forms
from .models import Cita
from phonenumber_field.formfields import PhoneNumberField as PhoneFormField


class CitasForm(forms.ModelForm):
    """Form to create an appointment. Based on the Cita model & shown in citas.html"""

    # Override del campo phone para usar PhoneNumberField del form
    phone = PhoneFormField(
        region="MX",
        label="Teléfono de contacto",
        help_text="Formato: +52 55 1234 5678",
        error_messages={
            "invalid": "Ingrese un número de teléfono válido para México.",
            "required": "Este campo es obligatorio.",
        },
    )

    class Meta:
        model = Cita
        fields = [
            "name",
            "email",
            "phone",
            "service",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configurar placeholders profesionales
        placeholders = {
            "name": "Ej: Juan Pérez García",
            "email": "ejemplo@correo.com",
            "phone": "+52 55 1234 5678",
            "service": "Seleccione un servicio",
            "description": "Describa brevemente el motivo de su cita...",
        }

        # Configurar labels más descriptivos
        labels = {
            "name": "Nombre completo",
            "email": "Correo electrónico",
            "phone": "Teléfono de contacto",
            "service": "Servicio solicitado",
            "description": "Descripción",
        }

        # Help texts personalizados
        help_texts = {
            "phone": "Incluya código de país (Ej: +52 para México)",
            "description": "Describa brevemente el motivo de su consulta",
        }

        # Aplicar configuración a cada campo
        for field_name, field in self.fields.items():
            # Placeholder
            if field_name in placeholders:
                field.widget.attrs["placeholder"] = placeholders[field_name]

            # Label personalizado
            if field_name in labels:
                field.label = labels[field_name]

            # Help text
            if field_name in help_texts:
                field.help_text = help_texts[field_name]

            # Accesibilidad
            field.widget.attrs.update(
                {
                    "aria-label": field.label,
                    "aria-required": "true" if field.required else "false",
                }
            )

            # ID único para asociar con label
            field.widget.attrs["id"] = f"id_{field_name}"

        # Configuración especial para el select de service
        self.fields["service"].empty_label = "Seleccione un servicio"
        self.fields["service"].queryset = (
            self.fields["service"].queryset.filter(activo=True)
            if hasattr(self.fields["service"].queryset.model, "activo")
            else self.fields["service"].queryset
        )

    def clean_phone(self):
        """Check if the phone number is valid for México. It must include the contry code, like '+52'."""
        phone = self.cleaned_data.get("phone")
        if phone:
            if not phone.is_valid():
                raise forms.ValidationError(
                    "El número de teléfono no es válido. "
                    "Asegúrese de incluir el código de país (+52 para México)."
                )
        return phone

    def clean_email(self):
        """Clean & check the email address. Converts to lowercase, removes spaces, & blocks temporary email domains."""
        email = self.cleaned_data.get("email")
        if email:
            # Normalizar email
            email = email.lower().strip()

            # Validar que no sea un email temporal/desechable (opcional)
            dominios_prohibidos = [
                "tempmail.com",
                "throwaway.email",
                "10minutemail.com",
            ]
            dominio = email.split("@")[-1].lower()

            if dominio in dominios_prohibidos:
                raise forms.ValidationError(
                    "Por favor, utilice un correo electrónico permanente."
                )

        return email

    def clean_name(self):
        """Check & format the full name. Makes sure it has at least two words (first & last name), & uses title case."""
        name = self.cleaned_data.get("name")
        if name:
            # Capitalizar correctamente
            name = name.strip().title()

            # Validar que tenga al menos nombre y apellido
            partes = name.split()
            if len(partes) < 2:
                raise forms.ValidationError(
                    "Por favor, ingrese su nombre completo (nombre y apellido)."
                )

        return name

    def clean_description(self):
        """Check the description field. Removes extra spaces & checks that it has at least 10 characters."""
        description = self.cleaned_data.get("description")
        if description:
            description = description.strip()

            # Validar longitud mínima (opcional)
            if len(description) < 10:
                raise forms.ValidationError(
                    "Por favor, proporcione más detalles (mínimo 10 caracteres)."
                )

        return description

    def clean(self):
        """Extra checks that use more than one field. You can add custom logic here."""
        cleaned_data = super().clean()

        # Aquí puedes agregar validaciones que involucren múltiples campos
        # Por ejemplo, verificar disponibilidad del servicio, etc.

        return cleaned_data
