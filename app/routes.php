<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the Closure to execute when that URI is requested.
|
*/

Route::get('/',function(){
	return View::make('hello');
});


Route::post('/', function()
{
	return  DB::table('chats')->max('id');
});

Route::post('sendMessage', function()
{
	$message = new Chat;
	$message->user = Input::get('username');
	$message->message = Input::get('message');
	$message->save();
	return $message->id;
});
Route::post('getHistory', function()
{
	$last = Input::get('last');
	return  Chat::where('id','>',$last)->get();
});
