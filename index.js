
var ddbTable = 'ITEM';
var item_params = {
    TableName: ddbTable
}
// Amazon access
// Initialize the Amazon Cognito credentials provider
AWS.config.region = 'us-east-2'; // Region
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'us-east-2:81247ce0-374f-43cd-9e21-4de4cfeac123',
});

// Instantiate aws sdk service objects now that the credentials have been updated
var docClient = new AWS.DynamoDB.DocumentClient({
    region: 'us-east-2'
});

docClient.scan(item_params, onScan);
function onScan(err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    else {
        var count = 1;
        $("#item_list").html('<thead class="thead-dark"><tr><th scope="col" style="width: 3%">#</th><th scope="col" style="width: 5%">Name</th><th scope="col" style="width: 5%">Slot</th><th scope="col" style="width: 5%">Cost</th><th scope="col" style="width: 5%">Lifetime</th><th scope="col" style="width: 10%">Stat Effect</th><th scope="col" style="width: 20%">Special Effect</th><th scope="col" style="width: 45%">Description</th><th scope="col" style="width: 5%">Edit</th></tr></thead><tbody></tbody>');
        data.Items.forEach(function (item) {
            // produce a stat
            var stats = "";
            if (item.stat1[0] != 'None') {
                stat = item.stat1[0];
                change = item.stat1[1];
                stats += stat + " + " + change;
                stats += "<br>"
            }
            if (item.stat2[0] != 'None') {
                stat = item.stat2[0];
                change = item.stat2[1];
                stats += stat + " + " + change;
                stats += "<br>"
            }
            if (item.stat3[0] != 'None') {
                stat = item.stat3[0];
                change = item.stat3[1];
                stats += stat + " + " + change;
                stats += "<br>"
            }
            if (item.stat4[0] != 'None') {
                stat = item.stat4[0];
                change = item.stat4[1];
                stats += stat + " + " + change;
                stats += "<br>"
            }
            if (item.stat5[0] != 'None') {
                stat = item.stat5[0];
                change = item.stat5[1];
                stats += stat + " + " + change;
                stats += "<br>"
            }
            var range = `<th scope="row">${count}</th>`;
            var name = `<td>${item.name}</td>`;
            var slot = `<td>${item.slot}</td>`;
            var cost = `<td>${item.cost}</td>`;
            var lifetime = `<td>${item.lifetime}</td>`;
            var stats = `<td>${stats}</td>`;
            var special_effects = `<td>${item.special}</td>`;
            var description = `<td>${item.description}</td>`;
            var name_without_space = item.name.replace(/\s+/g, '');

            var button = `<td><button type="button" class="btn btn-primary" id = "${name_without_space}">edit</button></td>`

            var $a = $("<tr/>") // creates a div element
                .attr("id", name_without_space) // adds the id
                .html(range + name + slot + cost + lifetime + stats + special_effects + description + button);
            $("#item_list").append($a);
            count++;
            $(".btn#" + name_without_space).click(function () {
                $('#create_item').modal();
                $('#create_item').find('form #Name').val(item.name);
                $('#create_item').find('form #Cost').val(item.cost);
                $('#create_item').find('form #EquipmentSlot').val(item.slot);
                $('#create_item').find('form #Lifetime').val(item.lifetime);
                $('#create_item').find('form #Description').val(item.description);
                $('#create_item').find('form #SpecialEffect').val(item.special);
                $('#create_item').find('form #Stat1').val(item.stat1[0]);
                $('#create_item').find('form #Stat2').val(item.stat2[0]);
                $('#create_item').find('form #Stat3').val(item.stat3[0]);
                $('#create_item').find('form #Stat4').val(item.stat4[0]);
                $('#create_item').find('form #Stat5').val(item.stat5[0]);
                $('#create_item').find('form #Value1').val(item.stat1[1]);
                $('#create_item').find('form #Value2').val(item.stat2[1]);
                $('#create_item').find('form #Value3').val(item.stat3[1]);
                $('#create_item').find('form #Value4').val(item.stat4[1]);
                $('#create_item').find('form #Value5').val(item.stat5[1]);
            });
        });

        // continue scanning if we have more movies, because
        // scan can retrieve a maximum of 1MB of data
        if (typeof data.LastEvaluatedKey != "undefined") {
            console.log("Scanning for more...");
            params.ExclusiveStartKey = data.LastEvaluatedKey;
            docClient.scan(item_params, onScan);
        }
    }
}


function create_item() {
    name = $("#Name").val();
    description = $("#Description").val();
    cost = $("#Cost").val();
    equipment = $("#EquipmentSlot").val();
    lifetime = $("#Lifetime").val();
    stat1 = $("#Stat1").val();
    v1 = $("#Value1").val();
    stat2 = $("#Stat2").val();
    v2 = $("#Value2").val();
    stat3 = $("#Stat3").val();
    v3 = $("#Value3").val();
    stat4 = $("#Stat4").val();
    v4 = $("#Value4").val();
    stat5 = $("#Stat5").val();
    v5 = $("#Value5").val();
    special = $("#SpecialEffect").val();
    name = name == '' ? "default" : name;
    description = description == '' ? "Write Something here" : description;
    cost = cost == '' ? "0" : cost;
    equipment = equipment == '' ? "Hand" : equipment;
    lifetime = lifetime == '' ? "1" : lifetime;
    stat1 = stat1 == 'None' ? [stat1, '0'] : [stat1, v1];
    stat2 = stat2 == 'None' ? [stat2, '0'] : [stat2, v2];
    stat3 = stat3 == 'None' ? [stat3, '0'] : [stat3, v3];
    stat4 = stat4 == 'None' ? [stat4, '0'] : [stat4, v4];
    stat5 = stat5 == 'None' ? [stat5, '0'] : [stat5, v5];
    console.log(stat1, stat2, stat3, stat4, stat5);
    special = special == '' ? "None" : special;
    var params = {
        TableName: ddbTable,
        Item: {
            'name': name,
            'description': description,
            'cost': cost,
            'slot': equipment,
            'lifetime': lifetime,
            'stat1': stat1,
            'stat2': stat2,
            'stat3': stat3,
            'stat4': stat4,
            'stat5': stat5,
            'special': special
        }
    };

    docClient.put(params, function (err, data) {
        if (err) {
            console.log("Error", err);
            $('#success_inform').modal();
            $('#success_inform').find('.modal-title').text('Failure')
            $('#success_inform').find('.modal-body').html('<p>Fail to create item. Check network!.</p>')
        } else {
            console.log("Success", data);
            $('#success_inform').modal();
            docClient.scan(item_params, onScan);
        }
    });
}

$(document).ready(function () {
    $("#submit_button").click(function () {
        $("#create_item_form").submit();
    });

    $('#create_item').on('show.bs.modal', function (event) {
        $('#create_item_form').get(0).reset();
    })

});
