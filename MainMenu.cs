using Godot;
using System;

public partial class MainMenu : Node2D
{

	private Button btnStart;
	private Button btnStartStars;
	private Button btnQuit;
	private Button focusedButton;


	PackedScene scene = GD.Load<PackedScene>("res://star_enemy.tscn");
	public override void _Ready()
	{
		btnStart = GetNode<CanvasLayer>("CanvasLayer").GetNode<Button>("ButtonNew");
		btnStartStars = GetNode<CanvasLayer>("CanvasLayer").GetNode<Button>("ButtonNewStars");
		btnQuit = GetNode<CanvasLayer>("CanvasLayer").GetNode<Button>("ButtonQuit");
		btnStartStars.GrabFocus();
		btnStart.Pressed += HandleButtonStartPressed;
		btnStartStars.Pressed += HandleButtonStartStarsPressed;
		btnQuit.Pressed += HandleButtonQuitPressed;
		GetViewport().GuiFocusChanged += HandleButtonFocusChanged;
		focusedButton = btnStartStars;



	}

	public override void _Process(double delta)
	{
		if(Input.IsActionPressed("start"))

		{
			if (focusedButton != null) {
				focusedButton.EmitSignal("pressed");
			}
		}
	}


	private void HandleButtonFocusChanged(Control control)
	{
		focusedButton = (Button)control;
	}

	private void HandleButtonStartPressed()
	{
		var scene = ResourceLoader.Load<PackedScene>("res://mapa01.tscn").Instantiate();
		GetTree().Root.AddChild(scene);
		GetTree().Root.RemoveChild(this);
	}

	private void HandleButtonStartStarsPressed()
	{
		var scene = ResourceLoader.Load<PackedScene>("res://stars_map.tscn").Instantiate();
		GetTree().Root.AddChild(scene);
		GetTree().Root.RemoveChild(this);
	}

	private void HandleButtonQuitPressed()
	{
		GetTree().Quit();
	}

}
