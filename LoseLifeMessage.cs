using Godot;
using System; 

public partial class LoseLifeMessage : CanvasLayer
{
	private Label _label;
	private Button _button;
	private StarsMap _map;
	bool _gameOver = false;
	public override void _Ready()
	{
		_label = GetNode<CanvasLayer>("CanvasLayer").GetNode<ColorRect>("ColorRect").GetNode<Label>("MessageLabel");
		_label.ProcessMode = ProcessModeEnum.Always;
		_button = GetNode<CanvasLayer>("CanvasLayer").GetNode<ColorRect>("ColorRect").GetNode<Button>("ContinueButton");
		_button.ProcessMode = ProcessModeEnum.Always;
		_button.Pressed += OnContinueButtonPressed;
		GD.Print("_Ready Called");
	}

// You might want to customize the message based on lives or game over
	public void SetMessage(string message, StarsMap map)
	{
		_map = map;
		_gameOver = map.Hud.Lives == 0;
		GD.Print("SetMessage Called " + message);
		_label.Text = message;
	}

	// This method will be called when the "Continue" button is pressed
	private void OnContinueButtonPressed()
	{
		GD.Print("On Continue.");
		Continue();

	}

	private void Continue()
	{
		GD.Print("On Continue Pressed.");
		// Unpause the game
		GetTree().Paused = false;

		if (_gameOver)
		{
			_map.GameOver();
		}
		else
		{
			_map.ContinueGame();
		}

		// Hide or remove this UI scene
		QueueFree(); // Removes the scene from memory
		// Or, if you want to keep it and just hide: Visible = false;

		// If it's a "Game Over" button, you might want to restart the level or go to main menu
		// GetTree().ChangeSceneToFile("res://Scenes/main_menu.tscn");
		// GetTree().ReloadCurrentScene(); // Reloads the current scene
	}

	public override void _PhysicsProcess(double delta)
	{   
		GetInput();
	}

	private void GetInput()
	{
		if (Input.IsActionPressed("jump"))
		{
			Continue();
		}
	}
}
