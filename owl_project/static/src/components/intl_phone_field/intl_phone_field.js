/** @odoo-module **/
console.log("Se abrio");
import { registry } from "@web/core/registry";
import { onWillStart, useRef, useState, onMounted } from "@odoo/owl";
import { PhoneField } from "@web/views/fields/phone/phone_field";
import { loadCSS, loadJS } from "@web/core/assets";
import { useService } from "@web/core/utils/hooks";

export class Intl_phone_field extends PhoneField {

  setup() {
    super.setup();
    this.phoneInput = useRef('input');

    this.state = useState({
      iti: undefined,
      isValidNumber:false
    });

    this.notificationService=useService("notification");

    onWillStart(async () => {
      await loadCSS(
        'https://cdn.jsdelivr.net/npm/intl-tel-input@25.3.1/build/css/intlTelInput.css',
      );

      await loadJS(
        'https://cdn.jsdelivr.net/npm/intl-tel-input@25.3.1/build/js/intlTelInput.min.js',
      );
    });

    onMounted(() => {
      this.state.iti = intlTelInput(this.phoneInput.el, {
        loadUtils: () => import("https://cdn.jsdelivr.net/npm/intl-tel-input@25.3.1/build/js/utils.js"),
      });
    })
  }

  validate(){

    if(this.state.iti){
      this.state.isValidNumber=this.state.iti.isValidNumber();
    }

    if(this.state.isValidNumber){
      this.notificationService.add('El teléfono es válido',{
        title:'Validación de teléfono',
        type:'success',
        sticky:false,
        clasName:'rounded-3',
      });
    }else{
      this.notificationService.add('El teléfono no es válido',{
        title:'Validación de teléfono',
        type:'danger',
        sticky:false,
        clasName:'rounded-3',
      });
    }
  }

}

Intl_phone_field.template = "owl_project.Intl_phone_field";


registry.category("fields").add("intl_phone_field", {
  component: Intl_phone_field,
});