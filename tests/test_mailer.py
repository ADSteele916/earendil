"""Integration tests."""

from pytest_mock import MockerFixture

from earendil import send_markdown_email


def test_send_markdown_email(mocker: MockerFixture):
    server = mocker.Mock()

    sender_email = "sender@gmail.com"
    recipient = "receiver@example.com"
    subject = "Example Subject"
    message = "# This message is written in *Markdown*."

    send_markdown_email(server, sender_email, recipient, subject, message)
    server.send_message.assert_called_once()
