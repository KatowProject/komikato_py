<?php
$query = $_GET['q'];
if ($query == "") :
    header('Content-Type: application/json');

    echo json_encode([
        "status" => "error",
        "message" => "No query specified"
    ]);
    return;
endif;

$url = base64_decode($query);
$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$output = curl_exec($ch);
$getHeader = curl_getinfo($ch);

if ($getHeader["redirect_url"] != "") :
    $url = $getHeader["redirect_url"];
    curl_setopt($ch, CURLOPT_URL, $url);
    $output = curl_exec($ch);
endif;

if ($output === '') :
    $error = curl_error($ch);
    http_response_code(500);
    echo json_encode([
        "status" => "error",
        "message" => $error
    ]);
    return;
endif;
curl_close($ch);

header("Content-Type: " . $getHeader['content_type']);
echo $output;
