class countC{
    static count = 0;
    constructor(){
      this.instanceId = ++countC.count;
    }
}

function cloneMore(selector, type) {
    console.log("aaaaaaaa");
    var newElement = $(selector).clone(true);
    var a = new countC();
    var total = a.instanceId;
    console.log(total);
    var newId = 't_'+(total+1);
    newElement.find(':input').each(function() {
        var name = $(this).attr('name');
        var id = ('id_' + name).replace('0', total);
        console.log('me cago en todo');
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
        newElement.find("#td_" + '1').attr({'id':"td_" + (total+1)});
        newElement.find("#td_"+(total+1)).text(total+1);
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

