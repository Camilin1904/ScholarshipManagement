class countC{
    static count = 0;
    constructor(){
      this.instanceId = ++countC.count;
    }

}

function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var a = new countC();
    var total = newElement.find(".num").attr('id').replace("td_", "");
    total = parseInt(total)
    var newId = 't_'+(total+1);

    newElement.find(':input').each(function() {
        var name = $(this).attr('name');
        var id = ('id_' + name).replace('0', total);
        if($(this).attr('type') === 'button'){
            $(this).attr({'name': name, 'id': id, 'data-div':newId, style:'visibility:visible'});
        }
        else{
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        }
        
    });
    var oldId = 't_'+(total);

    newElement.attr({'id': newId});
    try{
        newElement.find("#td_" + (total)).attr({'id':"td_" + (total+1)});
        newElement.find("#td_"+(total+1)).text(total+2);
        console.log(newElement.find("#td_"+(total+1)));
    }
    catch (e){
        console.log(e); 
    }
    
    $('tr.table:last').after(newElement);
    
}
function deleteMyself(id){
    $(id).remove();
}


